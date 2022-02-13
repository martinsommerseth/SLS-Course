from src import bin_packing as bp

body = "{\n    \"weights\": [\n        48,\n        30,\n        19,\n        36,\n        36,\n        27,\n        42,\n        42,\n        36,\n        24,\n        30\n    ],\n    \"items\": [\n        0,\n        1,\n        2,\n        3,\n        4,\n        5,\n        6,\n        7,\n        8,\n        9,\n        10\n    ],\n    \"bins\": [\n        0,\n        1,\n        2,\n        3,\n        4,\n        5,\n        6,\n        7,\n        8,\n        9,\n        10\n    ],\n    \"bin_capacity\": 100\n}";
print(bp.solver({"body":body}, ""))
