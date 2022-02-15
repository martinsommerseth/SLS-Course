from __future__ import print_function
from ortools.linear_solver import pywraplp
import json


def solver(event, context):
    data = json.loads(event['body'])
    # Create the mip solver with the CBC backend.
    solver = pywraplp.Solver('bin_packing_mip',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}
    for i in data['items']:
        for j in data['bins']:
            x[(i, j)] = solver.IntVar(0, 1, 'x_%i_%i' % (i, j))

    # y[j] = 1 if bin j is used.
    y = {}
    for j in data['bins']:
        y[j] = solver.IntVar(0, 1, 'y[%i]' % j)

    # Constraints
    # Each item must be in exactly one bin.
    for i in data['items']:
        solver.Add(sum(x[i, j] for j in data['bins']) == 1)

    # The amount packed in each bin cannot exceed its capacity.
    for j in data['bins']:
        solver.Add(
            sum(x[(i, j)] * data['weights'][i] for i in data['items']) <= y[j] *
            data['bin_capacity'])

    # Objective: minimize the number of bins used.
    solver.Minimize(solver.Sum([y[j] for j in data['bins']]))

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        bins = []
        num_bins = 0.
        for j in data['bins']:
            if y[j].solution_value() == 1:
                bin_items = []
                bin_weight = 0
                for i in data['items']:
                    if x[i, j].solution_value() > 0:
                        bin_items.append(i)
                        bin_weight += data['weights'][i]
                if bin_weight > 0:
                    bin = {"Bin number": num_bins, "Items packed: ": bin_items,"Total weight":bin_weight}
                    bins.append(bin)
                    num_bins += 1
                    print('Bin number', j)
                    print('  Items packed:', bin_items)
                    print('  Total weight:', bin_weight)
                    print()
        print()
        print('Number of bins used:', num_bins)
        print('Time = ', solver.WallTime(), ' milliseconds')
        body = {
            "Bins": bins,
            "Number of bins used": num_bins,
            "Time (ms)": solver.WallTime()
        }
    else:
        print('The problem does not have an optimal solution.')
        body = {
            "message": 'The problem does not have an optimal solution.',
        }


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response