##
## EPITECH PROJECT, 2021
## 109titration
## File description:
## calc
##

import sys
import math

def calc_pns(data, derive):
	default = 0.0
	result = []
	result.append(1)
	result.append(0)
	for i in range(1, len(data) - 1):
		if default < derive[i]:
			default = derive[i]
			result[0] = data[i][0]
			result[1] = i
	return result

def calc_deriv(data):
	derive = []
	derive.append(0)
	print("Derivative:")
	for i in range(1, len(data) - 1):
		calc = data[i + 1][1] - data[i - 1][1]
		calc /= (data[i + 1][0] - data[i - 1][0])
		derive.append(calc)
		print("volume: %g ml -> %.2f" %(data[i][0], derive[i]))
	pns = calc_pns(data, derive)
	derive.append(0)
	print("\nEquivalent point at %g ml\n" % pns[0])
	return derive

def calc_deriv_bis(derive, data):
	print("Second derivative:")
	for i in range(1, len(derive) - 3):
		ph = (derive[i + 2] - derive[i])
		ph /= (data[i + 2][0] - data[i][0])
		print("volume: %g ml -> %.2f" % (data[i + 1][0], ph))
	print("\nSecond derivative estimated:")

def calc_deriv_bis_estimation(derive, data):
	pns = calc_pns(data, derive)
	recursive = pns[0]
	key = pns[1]
	it = data[key - 1][0]
	ph = 0
	one = 0
	result = []
	result.append(it)
	if not key - 2 < 0:
		ph = (derive[key] - derive[key - 2])
		ph /= (data[key][0] - data[key - 2][0])
		one = ph
	result.append(ph)
	result.append(one)
	two = (derive[key + 1] - derive[key - 1])
	two /= (data[key + 1][0] - data[key - 1][0])
	result.append(two)
	res = (two - one)
	res /= (10 * (data[key][0] - data[key - 1][0]))
	result.append(recursive)
	while result[0] - 0.05 < data[key][0]:
		print("volume: %g ml -> %.2f" % (result[0], result[2]))
		if math.fabs(result[1]) > math.fabs(result[2]) and key + 3 < len(data):
			result[1] = result[2]
			result[4] = result[0]
		result[2] += res
		result[0] += 0.1
	calc_deriv_bis_estimation_bis(result, derive, data)

def calc_deriv_bis_estimation_bis(result, derive, data):
	pns = calc_pns(data, derive)
	key = pns[1]
	it = result[0]
	ph = result[1]
	one = result[2]
	two = result[3]
	recursive = result[4]
	res = 0
	if key + 3 >= len(derive):
		res = -two / 10
	else:
		one = (derive[key + 2] - derive[key])
		one /= (data[key + 2][0] - data[key][0])
		res = (one - two)
		res /= (10 * (data[key + 1][0] - data[key][0]))
	two += res
	while it - 0.05 < data[key + 1][0]:
		print("volume: %g ml -> %.2f" % (it, two))
		two += res
		it += 0.1
		if math.fabs(ph) > math.fabs(two) and key + 3 < len(data):
			ph = two
			recursive = it
	print("\nEquivalent point at %g ml" % recursive)