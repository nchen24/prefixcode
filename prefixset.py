'''
    Short python exercise to find the min prefix code of set of data. Adapated
    from https://www.cs.duke.edu/csed/newapt/prefixcode.html
'''

class DataAndIndexPair:
    '''
        Pair representing data and its original index in a list. To be used when
        wanting to find the original index of an item, after sorting a list of
        such items.
    '''
    def __init__(self, data, original_index):
        self.data = data
        self.original_index = original_index
    def __lt__(self, other):
        return self.data < other.data

class InputSet:
    '''
        A set of data for finding the min prefix code of
    '''

    def __init__(self, input_set):
        self.inputs = []
        for i, data in enumerate(input_set):
            self.inputs.append(DataAndIndexPair(data, i))
        self.inputs = sorted(self.inputs)

    def find_min_prefix_code(self):
        prefix_codes = self.find_prefix_codes()
        if len(prefix_codes) == 0:
            return None
        original_indexes = [self.inputs[x].original_index for x in prefix_codes]
        return min(original_indexes)

    def find_prefix_codes(self):
        prefix_codes = set()
        for i in range(len(self.inputs)-1):
            if self.is_prefix_of_next(i): # If this element is prefix, discard
                prefix_codes.discard(i-1) # prev element, as it is a sub-prefix
                prefix_codes.add(i)
        return prefix_codes

    def is_prefix_of_next(self, index):
        return self.inputs[index+1].data.startswith(self.inputs[index].data)
            

def main():
    input_sets = [["trivial"],
                  ["10001", "011", "100", "001", "10"],
                  ["1010", "11", "100", "0", "1011"],
                  ["no", "nosy", "neighbors", "needed"],
                  ["No", "not"],
                  ["20002", "200", "10001", "022", "011", "100", "002", "20", "001", "10"]]

    for input in input_sets:
        print("Running for input:" + str(input))
        input_set = InputSet(input)
        min_prefix_code = input_set.find_min_prefix_code()
        if min_prefix_code == None:
            print("Yes\n")
        else:
            print("No, %d\n" % min_prefix_code)

if __name__ == "__main__":
    main()
