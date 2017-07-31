'''
    Short python exercise to find the min prefix code of set of data. Adapated
    from https://www.cs.duke.edu/csed/newapt/prefixcode.html

    Versions of functions that avoid using python specific syntax are prefixed
    with ez_ (e.g. __ez_init__)
'''


class DataAndIndexPair:
    '''
        Pair representing data and its original index in a list. To be used when
        wanting to find the original index of an item, after sorting a list of
        such items.
    '''
    def __init__(self, data, original_index):
        '''
            Constructor for DataAndIndexPair
            Parameters:
                data: The data to store (any type)
                original_index: The index of the data in its original list (int)
            Return:
                A new DataAndIndexPair
        '''
        self.data = data
        self.original_index = original_index

    def __lt__(self, other):
        '''
            Defines the less-than operator for DataAndIndexPair.  Gets called
            when sorting, etc.
        '''
        return self.data < other.data


class InputSet:
    '''
        A set of data for finding the min prefix code of
    '''

    ##### Constructor #####
    def __init__(self, input_set):
        '''
            Constructor for InputSet
            Parameters:
                input_set: The list to find the minimum prefix code of (list of string)
            Return:
                A new InputSet

        '''
        self.inputs = []
        for i, data in enumerate(input_set):
            self.inputs.append(DataAndIndexPair(data, i))
        self.inputs = sorted(self.inputs)

    def __ez_init__(self, input_set):
        self.inputs = []
        for i in range(len(input_set)):
            self.inputs.append(DataAndIndexPair(input_set[i], i))
        self.inputs = sorted(self.input)

    ##### Find minimum prefix code #####
    def find_min_prefix_code(self):
        '''
            Find the minimum prefix code in the input set
            Parameters:
                None
            Return:
                The minimum prefix code of input_set, or None, if no prefix code
                exists.
        '''
        prefix_codes = self.find_prefix_codes()
        if len(prefix_codes) == 0:
            return None
        original_indexes = [self.inputs[x].original_index for x in prefix_codes]
        return min(original_indexes)

    def ez_find_min_prefix_code(self):
        prefix_codes = self.find_prefix_codes()
        if len(prefix_codes) == 0:
            return None

        original_indexes = []
        for prefix_code in prefix_codes:
            original_indexes.append(self.inputs[prefix_code].original_index)
        return min(original_indexes)

    ##### Find prefix codes #####
    def find_prefix_codes(self):
        '''
            Find all prefix codes in input set.  Because we have guaranteed the
            input set to be sorted (in the constructor), we don't need to check
            if the last element is a prefix code.  This is because when strings
            are sorted, prefixes always come before full words.  In other words,
            "pre" should always come before "prefix" in sorting, because "prefix"
            has additional letters
            Parameters:
                None
            Return:
                All prefix codes in input_set, or an empty set if none exist
        '''
        prefix_codes = set()
        for i in range(len(self.inputs)-1):
            if self.is_prefix_of_next(i):  # If this element is prefix, discard
                prefix_codes.discard(i-1)  # prev element, as it is a sub-prefix
                prefix_codes.add(i)
        return prefix_codes

    def ez_find_prefix_codes(self):
        prefix_codes = set()
        for i in range(len(self.inputs-1)):
            if(self.ez_is_prefix_of_next(i)):
                prefix_codes.discard(i-1)
                prefix_codes.add(i)
        return prefix_codes

    ##### Is prefix of next #####
    def is_prefix_of_next(self, index):
        '''
            Determine whether index'th element in input_set is a prefix of
            index+1'th.
            Parameters:
                index: The index to check (int)
            Return:
                True of index is a prefix of index+1, false otherwise
        '''

        return self.inputs[index+1].data.startswith(self.inputs[index].data)

    def ez_is_prefix_of_next(self, index):
        current_element = self.inputs[index]
        next_element = self.inputs[index+1]
        if next_element.startswith(current_element):  # Built in python string function
            return True
        return False


def main():
    # Making a list of input_sets to test
    input_sets = [["trivial"],
                  ["10001", "011", "100", "001", "10"],
                  ["1010", "11", "100", "0", "1011"],
                  ["no", "nosy", "neighbors", "needed"],
                  ["No", "not"],
                  ["20002", "200", "10001", "022", "011", "100", "002", "20", "001", "10"]]

    for input in input_sets:
        print("Running for input:" + str(input))  # Print the set for easy viewing
        input_set = InputSet(input)  # Create an InputSet
        min_prefix_code = input_set.find_min_prefix_code()  # Find its minimum prefix code
        if min_prefix_code == None:  # If no prefix codes exist, this is a prefix set
            print("Yes\n")
        else:  # If one does exist, print the index of the minimum prefix code
            print("No, %d\n" % min_prefix_code)  # Same as print("No, " + min_prefix_code + "\n")


if __name__ == "__main__":
    '''
        Start reading code here
    '''
    main()
