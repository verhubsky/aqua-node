from core.feeder import AutoFeeder
from core.fish import FishBatch
from core.pool import Pool

# Fish batches
f1 = FishBatch(
    species="Карась",
    count=300,
    avg_weight=500.0,
)

f3 = FishBatch(
    species="Окунь",
    count=248,
    avg_weight=375.0,
)

f2 = FishBatch(
    species="Осётр",
    count=50,
    avg_weight=1000.0,
)


# Auto feeders
fdr1 = AutoFeeder(
    capacity=600.0,
    current_load=574.9,
    daily_rate=128.7,
)

fdr2 = AutoFeeder(
    capacity=1500.0,
    current_load=290.8,
    daily_rate=364.3,
)

fdr3 = AutoFeeder(
    capacity=750.0,
    current_load=589.4,
    daily_rate=145.2,
)


# Pools
p1 = Pool(
    pool_id=1,
    oxygen_level=92.8,
    pollution_level=13.3,
    fishes=f1,
    feeder=fdr1,
)

p2 = Pool(
    pool_id=2,
    oxygen_level=17.9,
    pollution_level=68.97,
    fishes=f2,
    feeder=fdr2,
)

p3 = Pool(
    pool_id=3,
    oxygen_level=77.4,
    pollution_level=39.7,
    fishes=f3,
    feeder=fdr3,
)
