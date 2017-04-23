from modules.primesieve import generate_primes


def generate_blocks(primes_file, blocks_file, block_size, blocks, primes_in_line):
    offset_table = 1

    stop_counter = 1
    blocks_counter = 1

    # Очень важно, чтобы в файле было ровно чисел, т.е. на каждую строку по primes_in_line
    with open(primes_file, 'r') as f_primes:
        with open('blocks/table.txt', 'w') as f_table:
            first_time = True
            new_line = False
            with open(blocks_file, 'w') as f_block:
                for line in f_primes:
                    line = line.split(' ')

                    if len(line) < primes_in_line:  # TODO: Костыль
                        break

                    line = [int(num.strip()) for num in line]

                    i = 0

                    while True:
                        if i + 1 == primes_in_line:  # Здесь понимаем, что нужно взять следующую строку
                            new_line = True
                            break

                        if new_line:  # По особому обрабатываем новую строку с числами
                            current_num = next_num
                            next_num = line[i]

                            i -= 1  # Чтобы получить верное смещение на следующей итерации
                            new_line = False
                        else:
                            current_num = line[i]
                            next_num = line[i + 1]

                        # print(current_num, next_num, 'now')

                        if first_time:
                            f_block.write('{} {} '.format(current_num, next_num - current_num))

                            if offset_table % primes_in_line == 0:
                                f_table.write('{}\n'.format(current_num))

                            f_table.write('{} '.format(current_num))

                            offset_table += 1
                            first_time = False
                        elif stop_counter + 1 != block_size:  # Последнее число в блоке писать нет смысла
                            f_block.write('{} '.format(next_num - current_num))

                        i += 1
                        stop_counter += 1

                        if stop_counter == block_size:
                            f_block.write('\n')

                            stop_counter = 1
                            blocks_counter += 1
                            first_time = True

                    if blocks_counter == blocks:
                        break


def split(blocks_file, blocks):
    files_counter = 1
    blocks_counter = 1

    need_new_file = True

    with open(blocks_file, 'r') as f_blocks:
        for block in f_blocks:
            if need_new_file:
                f = open('blocks/{}.txt'.format(files_counter), 'w')
                need_new_file = False

            f.write(block)

            if blocks_counter == blocks:
                f.close()

                files_counter += 1
                blocks_counter = 1
                need_new_file = True

            blocks_counter += 1

if __name__ == "__main__":
    N = 10 ** 10
    numbers_in_line = 10
    ps_file = '10**10_primes.txt'

    # generate_primes(N, ps_file)

    b_file = 'blocks/all_blocks.txt'
    bs = 10 ** 6
    b_size = 10 ** 4

    # generate_blocks(ps_file, b_file, b_size, bs, numbers_in_line)

    split(b_file, b_size)
