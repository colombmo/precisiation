from itertools import combinations


def accuracy(ground_truth=[], algorithm=[]):
	# Weighted distance between the two https://theory.stanford.edu/~sergei/papers/www10-metrics.pdf
	d = kendall_distance(ground_truth, algorithm)
	
	# Worst possible prediction of the algorithm, with this ground truth
	d_max = kendall_distance(sorted(ground_truth), [len(ground_truth)-i for i,g in enumerate(ground_truth)])
	
	# Normalized distance
	dist = d/d_max
	
	# Similarity (=accuracy)
	return 1 - dist

'''
# gt_order : list with the scores from the ground truth
# algo_order : list with the scores from precisiation algorithm
# The scores at the same position in the lists correspond to the same word
# Not normalize yet
'''
def kendall_distance(gt_order, algo_order):
	gt = combinations(gt_order,2)
	algo = combinations(algo_order,2)
	
	dt = zip(gt, algo)
	
	inversions = [(((d[0][0] > d[0][1]) and (d[1][0] < d[1][1])) or 
					((d[0][0] < d[0][1]) and (d[1][0] > d[1][1]))) * abs(d[0][0]-d[0][1]) * abs(d[1][0]-d[1][1])
					for d in dt]
	
	return sum(inversions)
		
def main():
	gt, algo = [1.0952380952380953, 2.4761904761904763, 2.4285714285714284, 4.0], [1.0000102524276104, 3.99842134482142, 2.0000158876397682, 3.001552515403994]
	
	print("Accuracy: "+str(accuracy(gt, algo)))
	
if __name__ == "__main__":
	main()