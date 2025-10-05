#include <SDL.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdio.h>

#define WIDTH  980 // 1800
#define HEIGHT 880 // 1169 
#define R1 50
#define R2 100
#define K2 5000 
#define K1 WIDTH * K2 * 3/(8*(R1+R2))
#define X_OFFSET WIDTH/2
#define Y_OFFSET HEIGHT/2

int distance = 0;
float A = 0, B = 0;
SDL_Window *window;
SDL_Renderer *renderer;

#define ASSERT(_e, ...) if (!(_e)) { fprintf(stderr, __VA_ARGS__); exit(1); }

static void init_SDL() {
	ASSERT(
		SDL_Init(SDL_INIT_VIDEO) == 0, 
		"Failed to SDL initialize: %s\n", 
		SDL_GetError());

	window = SDL_CreateWindow(
		"Donut", 
		SDL_WINDOWPOS_UNDEFINED, 
		SDL_WINDOWPOS_UNDEFINED,
		WIDTH, 
		HEIGHT,
		SDL_WINDOW_SHOWN);

	ASSERT(
		window != NULL, 
		"Failed to create window: %s\n",
		SDL_GetError());

	/* SDL_SetWindowFullscreen(window, SDL_WINDOW_FULLSCREEN_DESKTOP); */

	renderer = SDL_CreateRenderer(
		window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);

	ASSERT(
		renderer != NULL, 
		"Failed to create renderer: %s",
		SDL_GetError());
}

void draw(SDL_Renderer *renderer, int i,  int x, int y) {
	SDL_Rect pixel = {x + X_OFFSET, y + Y_OFFSET, 2, 2};	
    SDL_SetRenderDrawColor(renderer, i, i, i, 255);


    SDL_RenderFillRect(renderer, &pixel);
}

int main(int argc, char *argv[]) {
	init_SDL();	

    SDL_Event event; bool isRunning = true;
    while (isRunning == true) {
		while (SDL_PollEvent(&event)) {
			switch (event.type) {
			case SDL_QUIT:
				isRunning = false;
			case SDL_KEYDOWN:
				if (event.key.keysym.sym == SDLK_q)
					isRunning = false;
				if (event.key.keysym.sym == SDLK_w)
					distance -= 150;
				if (event.key.keysym.sym == SDLK_s) 
					distance += 150;
			}
		}

		SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
		SDL_RenderClear(renderer);  

		float cosB = cos(B), sinB = sin(B);
		float cosA = cos(A), sinA = sin(A);

		for (int t = 0; t < 628; t += 10) {
			float cosT = cos((float) t / 100), sinT = sin((float) t / 100);
			int x = R2 + R1 * cosT;
			int y = R1 * sinT;
			for (int p = 0; p < 628; p += 5) {
				float cosP = cos((float) p / 100), sinP = sin((float) p / 100);
            	float x2 = x * (cosB * cosP + sinA * sinB * sinP) - y * cosA * sinB;
				float y2 = x * (cosP * sinB - cosB * sinA * sinP) + y * cosA * cosB;
            	float z = distance + K2 + (R1 * sinA * sinT + cosA * sinP * x);
				float ooz = 1 / z;

				int xp = floor(x2 * K1 * ooz);
				int yp = floor(-y2 * K1 * ooz);

				float l = 
					cosP * cosT * sinB - cosA * cosT * sinP - sinA * sinT 
					+ cosB * (cosA * sinT - cosT * sinA * sinP) ;

				if (l > 0) {
					int luminance_index = round(l * 180); // 0 ~ 255
					draw(renderer, luminance_index, xp, yp);
				}
			}
		}

		if (A != 2) {
			A -= 0.004;
			B += 0.002;
		} else {
			A = 0;
			B = 0;
		}

		SDL_RenderPresent(renderer); 
    }

    SDL_DestroyWindow(window);
    SDL_DestroyRenderer(renderer);
	SDL_Quit();
	return 0;
}
