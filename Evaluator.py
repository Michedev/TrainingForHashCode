import sys

import InputParser

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'ERROR in EXEC: python Evaluator.py <config> <submission>'
        exit()

    fln_config = sys.argv[1]
    fln_submission = sys.argv[2]

    config = InputParser()
    config.loadInput(fln_config)

    print(config)
