# The-Trends-in-Original-Media

## Background and Overview

The media and entertainment industry has undergone rapid expansion with the rise of global streaming platforms. The proliferation of content across multiple formats—films, television series, and short productions—has created both opportunities and challenges in understanding what drives audience engagement and critical reception.

This dataset captures a cross-section of information from IMDb, including identifiers, titles, content type, production studio, audience ratings, vote counts, genres, release years, and runtime (where available). Together, these variables provide a structured foundation for analyzing patterns in content creation and performance.

The primary objective of this project is to extract insights that highlight:

- The distribution of content types and production volumes across studios.

- The relationship between audience ratings, popularity (votes), and content genres.

- Trends in release frequency and runtime characteristics over time.

- Comparative performance of major studios and platforms.

By focusing on measurable outcomes such as ratings, popularity, and production diversity, the analysis is designed to surface actionable insights with direct implications for content strategy, platform differentiation, and audience targeting.

This work also establishes a framework for future extensions, including the integration of external performance indicators (such as revenue data or streaming hours) and predictive modeling to anticipate audience reception.

## Data Structure Overview
The dataset was compiled from IMDb based on original productions from Netflix, Hulu, Amazon, Disney, and HBO. After appending and cleaning the CSV files, the data was imported into MySQL for structured analysis.

Three main tables were created:

- Everything – core information (IMDb ID, title, type, studio, rating, votes, runtime, year).

- Genre – a relational table linking each IMDb ID with one or more genres.

- TV Show Status – indicates whether a series was canceled or concluded.

This relational setup supports detailed trend, genre, and status analysis across platforms.

![](Images/Screenshot%202025-09-22%20120030.png)

*Genres were parsed from the IMDb dataset by separating multi-genre entries (delimited by commas) into distinct categories. This ensured that each title could be accurately linked to multiple genres for more granular analysis.

## 3. Executive Summary

The analysis highlights that Netflix holds a disproportionately large share in the creation of original content. However, given the platform’s strategic reliance on original productions, simple volume comparisons with other studios would present an incomplete picture. To maintain clarity and focus, this project narrows its scope to two areas of particular interest: the animation genre and television series, allowing for a more balanced and meaningful exploration of trends.

![](Images/newplot(8).png)
![](Images/newplot(7)-imageonline.co-merged.png)

to see these charts yourslef click ![here1](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/pie_by_origin.html) , ![here2](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/pie_by_type.html), ![here3](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/pie_total_origin.html)

### Summery Overview
