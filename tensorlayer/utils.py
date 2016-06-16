## Evaluation
def evaluation(y_test, y_predict, n_classes):
    """Input the predicted results, targets results and
    the number of class, return the confusion matrix, F1-score of each class,
    accuracy and macro F1-score.

    Parameters
    ----------
    y_test : numpy.array or list
        target results
    y_predict : numpy.array or list
        predicted results
    n_classes : int
        number of classes

    Examples
    --------
    >>> dp_dict = Layer.dict_to_one( network.all_drop )
    >>> dp_dict = Layer.dict_to_one( network.all_drop )
    >>> feed_dict.update(dp_dict)
    """
    from sklearn.metrics import confusion_matrix, f1_score, accuracy_score
    c_mat = confusion_matrix(y_test, y_predict, labels = [x for x in range(n_classes)])
    f1    = f1_score(y_test, y_predict, average = None, labels = [x for x in range(n_classes)])
    f1_macro = f1_score(y_test, y_predict, average='macro')
    acc   = accuracy_score(y_test, y_predict)
    print('confusion matrix: \n',c_mat)
    print('f1-score:',f1)
    print('f1-score(macro):',f1_macro)   # same output with > f1_score(y_true, y_pred, average='macro')
    print('accuracy-score:', acc)
    return c_mat, f1, acc, f1_macro

def dict_to_one(dp_dict):
    """Input a dictionary, return a dictionary that all items are set to one, use for disable dropout, dropconnect layer and so on.

    Parameters
    ----------
    dp_dict : dictionary
        keeping probabilities

    Examples
    --------
    >>> dp_dict = Layer.dict_to_one( network.all_drop )
    >>> dp_dict = Layer.dict_to_one( network.all_drop )
    >>> feed_dict.update(dp_dict)
    """
    return {x: 1 for x in dp_dict}
