import mnist
import keras


def load_dataset():
	(trainx, trainy), (testx, testy) = mnist.load_data()
	trainx = trainx.reshape((trainx.shape[0], 28, 28, 1))
	testx = testx.reshape((testx.shape[0], 28, 28, 1))

	trainy = to_categorical(trainy)
	testy = to_categorical(testy)

	return trainx, trainy, testx, testy
