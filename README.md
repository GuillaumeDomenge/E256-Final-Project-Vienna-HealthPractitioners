# Analysis of Healthcare Providers’ Distribution in Vienna

Final project for **IEOR 256** by Guillaume Domenge (February 2025).

This project examines whether healthcare providers in Vienna are distributed in line with the city’s population, identifies specialty-level gaps across districts, and proposes a method for prioritising and locating additional practitioners.

## Data sources

- **Healthcare-provider locations:** a Vienna practitioner dataset originally sourced from [Praxisplan](https://www.praxisplan.at/) and downloaded from Kaggle.
- **Population data:** Vienna census data from the [Austrian Statistical Database (STATcube)](https://statcube.at/).

## Analysis

The report follows four stages:

1. Maps practitioner GPS coordinates and assigns each provider to a Vienna district.
2. Compares district-level practitioner counts with population, using doctors per 1,000 residents.
3. Studies the distribution of high-volume specialties. Paediatrics are scaled by the population under 14; general medicine is scaled by the population aged 14 and above.
4. Normalises each district’s specialty density against the city-wide average for that specialty, allowing shortages to be compared across specialties.

The analysis finds that most districts have roughly 5–10 doctors per 1,000 people, while Innere Stadt is a substantial outlier at about 40. Population is generally informative for explaining provider distribution, but it does not fully explain it. Central business activity and daytime population may also contribute.

## Decision model

To allocate a fixed budget of new practitioners, the project uses a sequential allocation rule:

1. Identify the district/specialty pair with the lowest normalised density.
2. Add one hypothetical provider to that pair.
3. Recalculate the score and repeat until the available positions are allocated.

This directs additions to the greatest relative shortages. In the report’s comparison, psychiatry shows a less even distribution than general medicine and contains some of the largest relative shortfalls.

For within-district placement, the project minimises the aggregate distance from evenly sampled points in a district to their nearest practitioner. Because this objective is non-differentiable, it is solved with a genetic algorithm implemented using `pymoo`.

## Tools and libraries

- Python
- `overpy` / Overpass API for district-boundary data
- `shapely` for polygon operations and assigning providers to districts
- `pymoo` for genetic-algorithm optimisation

## Report

The complete report, including figures and the 100-practitioner allocation example, is available in [E256_Final_Project.pdf](E256_Final_Project.pdf).

## Limitations and future work

- The Praxisplan-derived provider dataset may not cover Vienna’s full healthcare landscape.
- The analysis lacks daytime-population and workplace-location data.
- City-wide averages are used as specialty targets; evidence-based targets would improve the allocation model.
- Within-district optimisation assumes a uniform population distribution. Incorporating population density would yield more realistic location recommendations.


Please read "E256_Final_project.pdf" for more information. 
