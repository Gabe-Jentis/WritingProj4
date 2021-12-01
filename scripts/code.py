import numpy as np
import matplotlib.pyplot as plt
import random
import argparse

#  Generate K reference points
def genRefPoints(k):
    ang = random.random() * 2 * np.pi
    points = np.zeros([k,2])
    for i in range(1,k+1):
        points[i-1] = [np.cos(ang + (2*i*np.pi)/k), np.sin(ang + (2*i*np.pi)/k)]
    return points


#  Get range measurement given point and reference point
def rangeMeasurement(pt, ref):
    d = np.sqrt(np.abs(pt[0]-ref[0])**2 + np.abs(pt[1]-ref[1])**2)
    noise = np.random.normal(0, 0.3)
    meas = d + noise
    while (meas < 0):
        noise = np.random.normal(0, 0.3)
        meas = d + noise
    return meas


def MAPlikelihood(measurements, candPt, refs):
    likelihood = 0
    K = len(refs)
    for k in range(K):
        likelihood += 1.0/K * (measurements[k] - np.sqrt(np.abs(candPt[0]-refs[k][0])**2 + np.abs(candPt[1]-refs[k][1])**2))**2
    likelihood += (0.3**2)/(K*(0.25**2)) * np.matmul(candPt, np.transpose(candPt))
    return likelihood


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This Program Creates a Contour Map to find the likelihood of the '
                                                 + 'position of a vehicle located in the unit circle based on noisy '
                                                 + 'measurements from a specified number of reference points')
    parser.add_argument('-refs', '--r', dest='numRefs', type=int, required=True,
                        help='Number of Reference Points')

    args = parser.parse_args()
    print(args.numRefs)
    # Define True Vehicle Location
    ang = random.random() * 2 * np.pi
    truePos = [np.cos(ang), np.sin(ang)]  # Random Point on unit circle radius 1

    # Scale to be somewhere inside unit circle
    truePos[0] = truePos[0] * random.random()
    truePos[1] = truePos[1] * random.random()
    print("The true position of the vehicle is: " + str(truePos))

    # Generate Grid to make contours
    delta = 0.005
    x = np.arange(-2.0, 2.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)

    refs = genRefPoints(args.numRefs)
    truePosRangeMes = [rangeMeasurement(truePos, r) for r in refs]
    likelihoods = np.zeros([len(X), len(Y)])
    for i in range(len(X)):
        for j in range(len(Y)):
            likelihoods[i, j] = MAPlikelihood(truePosRangeMes, [X[i][j], Y[i][j]], refs)

    print(MAPlikelihood(truePosRangeMes, truePos, refs))
    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, likelihoods, np.linspace(likelihoods.min(), likelihoods.max(), 30))
    ax.plot(truePos[0], truePos[1], 'r+', label='True Position')
    ax.plot([refs[i][0] for i in range(len(refs))], [refs[i][1] for i in range(len(refs))], 'bo',
            label='Reference point')
    ax.clabel(CS, inline=True, fontsize=10)
    ax.set_title('MAP Objective Function Contour Map: ' + str(args.numRefs) + ' Reference Point(s)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.legend()
    plt.show()
