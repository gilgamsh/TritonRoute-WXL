import os

# benchmark
class Benchmark:
    def __init__(self, full_name, abbr_name):
        self.full_name = full_name
        self.abbr_name = abbr_name
    def __repr__(self):
        return self.full_name

class Benchmarks:
    def __init__(self):
        self.__bms = []
        self.__bm_sets = dict()

    def add(self, full_name_pat, abbr_name_pat, ids):
        for id in ids:
            self.__bms.append(Benchmark(full_name_pat.format(id), abbr_name_pat.format(id)))

    def get_bm(self, name):
        for bm in self.__bms:
            if name == bm.abbr_name or name == bm.full_name:
                return bm
        print('Error: benchmark', name, 'cannot be found')
        quit()

    def add_set(self, set_name, bm_names):
        bms = []
        for name in bm_names:
            bms.append(self.get_bm(name))
        self.__bm_sets[set_name] = bms

    def get_choices(self):
        choices = []
        for bm in self.__bms:
            choices.append(bm.full_name)
            choices.append(bm.abbr_name)
        for bm_set in self.__bm_sets:
            choices.append(bm_set)
        choices.append('all')
        return choices

    def get_selected(self, names):
        if 'all' in names:
            return self.__bms
        else:
            selected = []
            for name in names:
                if name in self.__bm_sets:
                    selected += self.__bm_sets[name]
                else:
                    selected.append(self.get_bm(name))
            return selected


######################################
# Below is project-dependant setting #
######################################


# all benchmarks
all_benchmarks = Benchmarks()
all_benchmarks.add('ispd19_sample{}', '9s{}', ['', '2', '3', '4'])
all_benchmarks.add('ispd19_test{}', '9t{}', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
all_benchmarks.add('ispd18_sample{}', '8s{}', ['', '2', '3'])
all_benchmarks.add('ispd18_test{}', '8t{}', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

# Roughly speaking, each "fast" case take less than 30 min on proj53 with 8 threads
all_benchmarks.add_set('fast', ['9t1', '9t2', '9t3', '9t4', '9t5', '8t1', '8t2', '8t3', '8t4', '8t5', '8t6', '9s', '9s2', '9s3', '9s4', '8s', '8s2', '8s3'])
all_benchmarks.add_set('slow', ['9t6', '9t7', '9t8', '9t9', '9t10', '8t7', '8t8', '8t9', '8t10'])