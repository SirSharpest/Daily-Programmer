#include <stdio.h>
#include <stdlib.h>

float data[] = {9.20, 8.03, 10.02, 8.08, 8.14, 8.10, 8.31, 8.28,
                8.35, 8.34, 8.39, 8.45, 8.38, 8.38, 8.32, 8.36, 8.28,
                8.28, 8.38, 8.48, 8.49, 8.54, 8.73, 8.72, 8.76, 8.74,
                8.87, 8.82, 8.81, 8.82, 8.85, 8.85, 8.86, 8.63, 8.70,
                8.68, 8.72, 8.77, 8.69, 8.65, 8.70, 8.98, 8.98, 8.87,
                8.71, 9.17, 9.34, 9.28, 8.98, 9.02, 9.16, 9.15, 9.07,
                9.14, 9.13, 9.10, 9.16, 9.06, 9.10, 9.15, 9.11, 8.72,
                8.86, 8.83, 8.70, 8.69, 8.73, 8.73, 8.67, 8.70, 8.69,
                8.81, 8.82, 8.83, 8.91, 8.80, 8.97, 8.86, 8.81, 8.87,
                8.82, 8.78, 8.82, 8.77, 8.54, 8.32, 8.33, 8.32, 8.51,
                8.53, 8.52, 8.41, 8.55, 8.31, 8.38, 8.34, 8.34, 8.19,
                8.17, 8.16};


/*
 * Structure to hold possible combos
 */
struct Combo{

    float buy_price;
    float sell_price;

}; typedef struct Combo Combo;


//Define function to resize array

int main() {

    /*
     * Using the data provided we must select the smallest value
     * and the largest number
     *
     * The catch is that they must be done in chronological order
     * i.e. smallest number must not come after largest number
     */

    //Combination information
    int num_combos = 0;
    Combo *possible_combo = NULL;

    //Length of items
    int length_of_data = sizeof(data) / sizeof(data[0]);

    for (int i = 0; i < length_of_data ; ++i) {

        //For each element we want to compare it to
        //anything  2 slots of more ahead
        for (int j = (i+2); j < length_of_data ; ++j) {

            if(data[i] < data[j]){

                //create combo
                Combo c;
                c.buy_price = data[i];
                c.sell_price = data[j];

                //increment num_combos
                num_combos++;

                //allocate memory
                possible_combo = (Combo*) realloc(possible_combo, num_combos * sizeof(Combo));

                //assign combo
                possible_combo[num_combos-1] = c;

            }


        }

    }


    float best_buy, best_sell;

    for(int i = 0; i < num_combos; i++){

        if(i==0 ){
            best_buy = possible_combo[i].buy_price;
            best_sell = possible_combo[i].sell_price;
        }

        if( (possible_combo[i].sell_price - possible_combo[i].buy_price) >
                (best_sell - best_buy)){

            best_buy = possible_combo[i].buy_price;
            best_sell = possible_combo[i].sell_price;
        }

        if(i == num_combos-1){
            printf("Buy at: %f \t Sell at: %f\n", best_buy, best_sell );
        }
    }

    return 0;
}