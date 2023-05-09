import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from sksurv.datasets import load_whas500
x,target=load_whas500()
cols=["afb","mitype"]
df=(x[cols]
    .rename(columns={cols[0]:"v1",
                     cols[1]:'v2'})
    .astype(float))
df["event"],df["time"]=[list(i) for i in zip(*target)]

df.time=df.time.apply(lambda x: x+np.random.normal(2,1))
#sort observations by descending event time
df=df.sort_values("time",ascending=False).reset_index(drop=True)

print(df.head(10))
v=df[["v1","v2"]]
time,event=df.time.to_numpy(),df.event.to_numpy().astype(int)

def get_theta(x):
    """
    Return theta as per negative log-partial likehood
    of the cox model and its gradient
    :param x: beta coefficients
    :return:
    - theta_l:cumulative theta (numpy.ndarry）
    - theta_l_v:cumulative theta by features
    """
    theta=np.exp(np.dot(v,x))
    theta_l=np.cumsum(theta)
    theta_l_v=np.cumsum(v*theta.reshape(-1,1),axis=0)
    return theta_l,theta_l_v

def objective_function(x):
    theta_l,_=get_theta(x)
    return -np.sum(event*(np.dot(v,x)-np.log(theta_l)))

def gradient(x):
    """
    Return the gradient of the negative log-partial likelihood of the cox
    model
    :param x:
    :return:
    """
    theta_l,theta_l_v=get_theta(x)
    return -np.sum(event.reshape(-1,1)*(v-(theta_l_v/theta_l.reshape(-1,1))),axis=0)

beta=np.array([1,1])
opt_result=minimize(objective_function,beta,method="Newton-CG",jac=gradient)
print(opt_result)

from sksurv.linear_model import CoxPHSurvivalAnalysis

model = CoxPHSurvivalAnalysis()
model_fit = model.fit(
    df[["v1", "v2"]],
    np.array(list(zip(df.event, df.time)), dtype=np.dtype("bool, float")))

print(model_fit.coef_)


def objective_function_in_x(x0, x1):
    '''
    Return the negative log-partial likelihood
    of the Cox model evaluated in the given beta

    Args:
        - x0: input beta_0 <numpy.ndarray>
        - x1: input beta_1 <numpy.ndarray>
    Output:
        - objective function in beta_0, beta_1 <numpy.ndarray>
    '''
    v0, v1, l = v[:, 0], v[:, 1], v.shape[0]
    theta = np.exp(x0 * v0 + x1 * v1)
    return -np.sum(event * ((x0 * v0 + x1 * v1) - np.log(np.cumsum(theta).reshape(-1, l))))


def get_plot_data(inf=-5, sup=5, size=10):
    '''
    Return a three-dim square box with the evaluation
    of the negative log-partial likelihood of the Cox model

    Args:
      - inf: min value of the box, default: -5 <int>
      - sup: min value of the box, default: 5 <int>
      - size: size of the output coordinates arrays, default: 10 <int>
    Output:
      - x0: input beta_0 <numpy.ndarray>
      - x1: input beta_1 <numpy.ndarray>
      - z: objective function in beta_0, beta_1 <numpy.ndarray>
    '''
    x0, x1 = np.linspace(inf, sup, size), np.linspace(inf, sup, size)
    x0, x1 = np.meshgrid(x0, x1)
    z = np.zeros((size, size))
    for i in range(0, x0.shape[0]):
        for j in range(0, x0.shape[1]):
            z[i][j] = objective_function_in_x(x0[i][j], x1[i][j])
    return x0, x1, z


def get_min_obj_function(model):
    """

    :param model:
    :return:
    """
    '''
    Return coordinates of local optimum found with optimization

    Args:
      - model: instance of <scipy.optimize._optimize.OptimizeResult>
    Output:
      - x0: optimum for beta_0 <numpy.ndarray>
      - x1: optimum for beta_1 <numpy.ndarray>
      - z: objective function in the optimum <numpy.ndarray>
    '''
    x0, x1 = np.array(model.x[0]), np.array(model.x[1])
    z = objective_function_in_x(x0, x1)
    return x0, x1, z


# generate data
x0, x1, z = get_plot_data(-5, 5, 10)
x0_min, x1_min, z_min = get_min_obj_function(opt_result)

# plot the objective function and the local optimum
# fig = plt.figure(figsize=plt.figaspect(0.4))
#
# # left subplot
# ax = fig.add_subplot(1, 2, 1, projection="3d")
# ax.contour3D(x0, x1, z, 100, cmap="viridis")
# ax.scatter(x0_min, x1_min, z_min, marker="o", color="red", linewidth=50000)
# ax.set_xlabel("$β_1$")
# ax.set_ylabel("$β_2$")
# ax.set_zlabel("- Log-Partial Likelihood")
#
# # right subplot
# ax = fig.add_subplot(1, 2, 2, projection="3d")
# ax.contour3D(x0, x1, z, 100, cmap="viridis")
# ax.scatter(x0_min, x1_min, z_min, marker="o", color="red", linewidth=50000)
# ax.set_xlabel("$β_1$")
# ax.set_ylabel("$β_2$")
# ax.set_zlabel("- Log-Partial Likelihood")
# ax.view_init(10, 30)
# fig.suptitle("Negative log-partial likelihood of the Cox model with local optimum", fontsize=10);
#
