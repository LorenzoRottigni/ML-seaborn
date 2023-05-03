from sklearn.metrics import mean_absolute_error, accuracy_score, mean_squared_error, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import numpy as np
import seaborn as sns

y = np.random.random(size=100) * 10
errors = 2 * (np.randomm.random(size=100)) - 1
p = y + errors

mse = mean_squared_error(y, p)
maw = mean_absolute_error(y, p)

# Resiudal plot => check "what if tool"
res = y - p
sns.scatterplot(
    # on X axis of the graph there is y
    x=y,
    # on Y axis of the graph there is residual
    y=res
)

plt.show()