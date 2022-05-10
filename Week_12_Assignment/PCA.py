from PIL import Image
import numpy as np

#############################################
# PCA.py:                                   #
#                                           #
# This program implements the PCA algorithm #
# to perform compression on an image. Using #
# a differing number of eigenvectors, we    #
# can differ the level of compression.      #
#############################################
def PCA():
	# Open the image and convert it to an numpy array
	image = Image.open("./inputImageNotActuallyAPDF.bmp")
	arr = np.array(image)

	# print (str(arr))

	# Calculate the mean of each variable and subtract it
	# from the image
	image_mean = np.mean (arr, axis = 0)
	meaned_arr = arr - image_mean

	# Find the covariance matrix of the image
	covariance = np.cov(meaned_arr, rowvar = False)

	# Calculate the eigenvalues and eigenvectors
	eigenval, eigenvec = np.linalg.eigh(covariance)

	# Sort the eigenvalues by level of varience
	sort_index = np.argsort(eigenval)[::-1]
	sort_eigenval = eigenval[sort_index]

	# Sort eigenvectors by the same logic
	sort_eigenvec = eigenvec[:, sort_index]
	
	# Using a varying number of eigenvectors...
	numEigenVecToKeep = [15, 100, 200]
	for i in range (0, len(numEigenVecToKeep)):
		# Keep the first n eigenvectors for later
		eigensToKeep = np.zeros((len(sort_eigenvec[i]), numEigenVecToKeep[i]))
		print ('Creating image with ' + str(numEigenVecToKeep[i]) + ' eigenvectors...')
		
		# For all eigenvectors we are using...
		for j in range (0, numEigenVecToKeep[i]):
			# Calculate and print the percentage of varience for each eigenvector
			print ('Percentage of varience for eigenvector ' + str(j) + ': ' + str((sort_eigenval[j] / np.sum(sort_eigenval))*100))
		
		# Create the compressed image using n eigenvectors
		compressedImage = np.matmul (meaned_arr, eigensToKeep)

		# Decompressing the image by transposing by our eigenvectors and adding the mean back in
		lossyUnCompressedImage = np.matmul (compressedImage, np.transpose(eigensToKeep)) + image_mean

		# Make and show the image
		pil_im = Image.fromarray(lossyUnCompressedImage)
		pil_im.show()
PCA()
