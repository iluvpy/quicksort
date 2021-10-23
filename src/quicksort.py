from math import pi
import random


def item_from_left(array, pivot_index) -> int:
	for i in range(len(array)):
		if array[i] > array[pivot_index] and i != pivot_index:
			return i
	return pivot_index

def item_from_right(array, pivot_index) -> int:
	for i in range(2, len(array)):
		if array[-i] < array[pivot_index]:
			return len(array) - i
	return pivot_index

def quicksort(array, end=None):
	end_of_array = len(array) if end is None else end 
	pivot = end_of_array - 1 # pivot index
	print(f"pivot pos: {pivot}\npivot value: {array[pivot]}")
	
	done = False
	while not done:
		fl_index = item_from_left(array, pivot)
		fr_index = item_from_right(array, pivot)
		print("fl index ", fl_index)
		print("fr index ", fr_index)
		
		if fl_index > fr_index:
			done = True
			array[fl_index], array[pivot] = array[pivot], array[fl_index]
		else:
			array[fr_index], array[fl_index] = array[fl_index], array[fr_index]
	
	
	
def main():
	arr = [random.randint(0, 10) for _ in range(10)]
	print(f"before: {arr}")
	quicksort(arr)
	print(f"after: {arr}")

if __name__ == "__main__":
	main()