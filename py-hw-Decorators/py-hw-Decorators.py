from Decorators import param_decor

if __name__ == "__main__":
    @param_decor("log.txt")
    def adv_print(*args, start="", max_line=20, in_file=False):
        print_list = list()
        for i in args:
            print_list.append(i)
        print_list = start + " ".join([str(i) for i in print_list])
        outset = 0
        if not in_file:
            for i in range(int(len(print_list)/10)+1):
                print(print_list[outset:max_line])
                outset += 10
                max_line += 10
        else:
            f = open(in_file, "w")
            for i in range(int(len(print_list)/10)+1):
                print(print_list[outset:max_line])
                f.write(print_list[outset:max_line] + '\n')
                outset += 10
                max_line += 10
            f.close()
