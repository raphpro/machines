import logging
import multiprocessing as mp




# GLOBALS
counter = 0

machines = []

input_string = '11'





class State(object):

    def __init__(self):
        pass



class Q1(State):

    @staticmethod
    def transition_state(index, char, input_string_slice):
        logging.info(f'\n\t\t{__class__.__name__}.transition_state({index}, {char})')

        current_fsm = next((fsm for fsm in globals()['machines'] if fsm.index == index), None)
        logging.info(f'transition_state() accessing current fsm: fsm{current_fsm.index}')

        logging.info(f'fsm{current_fsm.index} in {__class__.__name__} receiving a {char} as input')

        if char == 0:
            current_fsm.current_state = 'Q1'
            logging.info(f'fsm{current_fsm.index} transitioning to state: {current_fsm.current_state}')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

        elif char == 1:
            logging.info(f'branch 1')

            current_fsm.current_state = 'Q1'
            logging.info(f'fsm{current_fsm.index} transitioning to state: {current_fsm.current_state}')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

            logging.info(f'branch 2')

            create_machine(str(__class__.__name__), input_string_slice)
            globals()['machines'][-1].current_state = 'Q2'
            logging.info(f'fsm{globals()["machines"][-1].index} transitioning to state: {globals()["machines"][-1].current_state}')
            globals()['machines'][-1].input_string_slice = globals()['machines'][-1].input_string_slice[1:]
            globals()['machines'][-1].computation_path.append(globals()["machines"][-1].current_state)
            logging.info(f'appending {globals()["machines"][-1].current_state} to fsm{globals()["machines"][-1].index} computation_path')
            logging.info(f'fsm{globals()["machines"][-1].index} computation_path: {globals()["machines"][-1].computation_path}')

        else:
            current_fsm.final_state = current_fsm.current_state
            current_fsm.current_state = 'dead'
            logging.info(f'fsm{current_fsm.index} is dead')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

        print('')



class Q2(State):

    @staticmethod
    def transition_state(index, char, input_string_slice):

        current_fsm = next((fsm for fsm in globals()['machines'] if fsm.index == index), None)

        # Account for the arrow showing the Empty Set:
        logging.info(f'state with empty set arrow encountered')
        logging.info(f'branching')

        create_machine('Q3', input_string_slice)
        globals()['machines'][-1].empty_arrow_origin = 'Yes'

        if char == 0:
            current_fsm.current_state = 'Q3'
            logging.info(f'fsm{current_fsm.index} transitioning to state: {current_fsm.current_state}')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

        else:
            current_fsm.final_state = current_fsm.current_state
            current_fsm.current_state = 'dead'
            logging.info(f'fsm{current_fsm.index} is dead')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

        print('')




class Q3(State):

    @staticmethod
    def transition_state(index, char, input_string_slice):

        current_fsm = next((fsm for fsm in globals()['machines'] if fsm.index == index), None)

        if char == 1:
            current_fsm.current_state = 'Q4'
            logging.info(f'fsm{current_fsm.index} transitioning to state: {current_fsm.current_state}')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

        else:
            current_fsm.final_state = current_fsm.current_state
            current_fsm.current_state = 'dead'
            logging.info(f'fsm{current_fsm.index} is dead')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

        print('')




class Q4(State):

    @staticmethod
    def transition_state(index, char, input_string_slice):

        current_fsm = next((fsm for fsm in globals()['machines'] if fsm.index == index), None)

        if char == 0 or char == 1:
            current_fsm.current_state = 'Q4'
            logging.info(f'fsm{current_fsm.index} transitioning to state: {current_fsm.current_state}')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

        else:
            current_fsm.final_state = current_fsm.current_state
            current_fsm.current_state = 'dead'
            logging.info(f'fsm{current_fsm.index} is dead')
            current_fsm.computation_path.append(current_fsm.current_state)
            logging.info(f'appending {current_fsm.current_state} to fsm{current_fsm.index} computation_path')
            logging.info(f'fsm{current_fsm.index} computation_path: {current_fsm.computation_path}')

        print('')




class Machine(object):

    states = {'Q1', 'Q2', 'Q3', 'Q4'}

    alphabet = {}

    accept_states = {'Q4'}


    def __init__(self, start_state, input_string_slice):

        self.index = globals().get('counter')

        self.start_state = ''

        self.current_state = start_state

        self.final_state = ''

        self.computation_path = [start_state]

        self.input_string = input_string_slice

        self.input_string_slice = input_string_slice

        self.empty_arrow_origin = ''



# -------------------------------------
def create_machine(start_state, input_string_slice):
    logging.info(f'\n\t\tcreate_machine({start_state})')

    fsm = Machine(start_state, input_string_slice)
    print(f'creating Machine {fsm.index}')

    if 'fsm' in locals():
        logging.info(f'fsm{fsm.index} = {locals().get("fsm")}')
    else:
        logging.info('no machine created')

    globals()['machines'].append(fsm)

    if fsm in globals()['machines']:
        logging.info(f'fsm{fsm.index} added to machines list: {globals()["machines"][-1]}')
    else:
        logging.info(f'fsm not added to machines')

    logging.info(f'machines: fsm{", fsm".join([str(machine.index) for machine in globals()["machines"]])}')

    globals()['counter'] += 1
    logging.info(f'counter = {counter}')





# -------------------------------------
def run_machines(input_string):

    logging.info(f'\n\t\trun_machine()')

    completes = []

    if 'completes' in locals():
        logging.info(f'local completes list established')
        logging.info(f'completed runs: {locals().get("completes")}')
    else:
        logging.info('no local completes created')


    for fsm in globals()['machines']:
        logging.info(f'\n\t\tLoop A: looping thru global machines list')
        logging.info(f'analyzing fsm{fsm.index}')


        if fsm.index in completes:
            logging.info(f'fsm {fsm.index} already completed')
            continue

        else:
            # Parse the string
            input_string = fsm.input_string_slice
            logging.info(f"machine's input string: {input_string}")

            for char in input_string[:]:
                logging.info(f'\n\t\tLoop B: looping thru input string for fsm{fsm.index}')
                logging.info(f'fsm{fsm.index} current state: {fsm.current_state}')

                logging.info(f'inputting {char} into fsm{fsm.index}')
                char = int(char)


                if fsm.current_state == 'dead':
                    logging.info(f'fsm {fsm.index} has died')
                    completes.append(fsm.index)
                    logging.info(f'computation path for fsm{fsm.index} now complete\n')

                    logging.info(f'Loop B broken')
                    break

                else:
                    # Use the current state of the machine to determine which meth to use:
                    state = globals().get(str(fsm.current_state))
                    logging.info(f'accessing {fsm.current_state}')

                    # Call the state's static transition_state() meth:
                    logging.info(f'calling {fsm.current_state}.transition_state({fsm.index}, {char})')
                    state.transition_state(fsm.index, char, input_string)

                input_string = input_string[1:]
                logging.info(f'remaining input string: {input_string}')


            completes.append(fsm.index)
            logging.info(f'computation path for fsm{fsm.index} now complete\n')





# -------------------------------------
def read_machines():
    final_states = []
    dead_machines = []
    accepted_machines = []
    unaccepted_machines = []

    logging.info(f'now reading final results...\n')
    for fsm in globals()['machines']:

        print(f'Machine {fsm.index} input string: {fsm.input_string}')

        if fsm.empty_arrow_origin != '':
            print(f'Machine {fsm.index} originated from empty set arrow')

        final_states.append(fsm.current_state)

        if fsm.current_state == 'dead':
            dead_machines.append(fsm.index)
        elif fsm.current_state in Machine.accept_states:
            accepted_machines.append(fsm.index)
            print(f'Machine {fsm.index}: Yay!')
        else:
            unaccepted_machines.append(fsm.index)
            print(f'Machine {fsm.index}: not accepted')


        print(f'Machine {fsm.index} tree: {fsm.computation_path}')

    print(f'final states: {final_states}')
    print(f'dead machines: {dead_machines}')
    print(f'unaccepted machines: {unaccepted_machines}')
    print(f'accepted machines: {accepted_machines}')


    if len(accepted_machines) > 0:
        print('input accepted')
    else:
        print('input rejected')


# -------------------------------------
if __name__ == "__main__":

    logging.basicConfig(format='\t\t%(message)s', level=logging.DEBUG)
    logging.info('engaging main program')

    logging.info(f'counter established')
    logging.info(f'counter = {counter}')
    logging.info(f'machines list established')
    logging.info(f'machines: {machines}')

    create_machine('Q1', globals().get('input_string'))
    run_machines(globals().get('input_string'))
    read_machines()






#
# END #
#
