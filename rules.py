
def rules():
    """
    Defines rules for grammar in form of list of tuples.

    Returns
    -------
    tuple[0]: grammar routine in regexp form
        This grammar routine would be used an index to search for
        the corresponding rule.

    tuple[1]: subject
        defines the subject of an action. e.g, in sentence 'Usman
        has 5 apples', 'Usman' is the subject. 

        Lists allowed.

    tuple[2]: operation
        defines the operation in actions. e.g, in sentence 'Usman
        has 5 apples', action is 'retain'; in sentence 'Usman gives
        away an apple', action is 'add'.
    
    tuple[3]: operation element
        defines the element that is used in operation. e.g, in 
        sentence 'Usman has two apples', 'two' is operation element.

    tuple[4]: primary object
        defines the primary object of an action. e.g, in sentence 
        'Usman gives 5 apples to Ali', 'apple' is the primary object.

    tuple[5]: secondary object
        defines the secondary object of an action. e.g, in sentence 
        'Usman gives 5 apples to Ali', 'Ali' is the secondary object.       

    tuple[6]: accuracy
        this index is used to evaluate which grammar rules are te most
        accuracy. Value is in interval [0,1]

    """
    rules = [
    [("A: {<DT>?<JJ>*<NN.+><RB>?<VBZ><CD>*<DT>?<JJ>*<NN.*>}"),(['NNP','NNPS']),('RETAIN'),('CD'),(['NN','NNS']),('None'),(1)]
    ]

    return rules
