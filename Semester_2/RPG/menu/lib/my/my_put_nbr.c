/*
** EPITECH PROJECT, 2020
** B-CPE-100-PAR-1-4-cpoolday07-luka.boudjelal
** File description:
** my_putnbr.c
*/

#include "my_bsq.h"

int my_put_nbr(int nb)
{
    if (nb < 0) {
        nb = nb * (-1);
        my_putchar('-');
    }
    if (nb < 10)
        my_putchar(nb + 48);

    if (nb >= 10) {
        my_put_nbr(nb / 10);
        my_put_nbr(nb % 10);
    }
    return 0;
}