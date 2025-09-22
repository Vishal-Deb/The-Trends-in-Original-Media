# The-Trends-in-Original-Media

## 1. Background and Overview

The media and entertainment industry has undergone rapid expansion with the rise of global streaming platforms. The proliferation of content across multiple formats—films, television series, and short productions—has created both opportunities and challenges in understanding what drives audience engagement and critical reception.

This dataset captures a cross-section of information from IMDb, including identifiers, titles, content type, production studio, audience ratings, vote counts, genres, release years, and runtime (where available). Together, these variables provide a structured foundation for analyzing patterns in content creation and performance.

The primary objective of this project is to extract insights that highlight:

- The distribution of content types and production volumes across studios.

- The relationship between audience ratings, popularity (votes), and content genres.

- Trends in release frequency and runtime characteristics over time.

- Comparative performance of major studios and platforms.

By focusing on measurable outcomes such as ratings, popularity, and production diversity, the analysis is designed to surface actionable insights with direct implications for content strategy, platform differentiation, and audience targeting.

This work also establishes a framework for future extensions, including the integration of external performance indicators (such as revenue data or streaming hours) and predictive modeling to anticipate audience reception.

## 2. Data Structure Overview
The dataset was compiled from IMDb based on original productions from Netflix, Hulu, Amazon, Disney, and HBO. After appending and cleaning the CSV files, the data was imported into MySQL for structured analysis.

Three main tables were created:

- Everything – core information (IMDb ID, title, type, studio, rating, votes, runtime, year).

- Genre – a relational table linking each IMDb ID with one or more genres.

- TV Show Status – indicates whether a series was canceled or concluded.

This relational setup supports detailed trend, genre, and status analysis across platforms.

![](Images/Screenshot%202025-09-22%20120030.png)

*Genres were parsed from the IMDb dataset by separating multi-genre entries (delimited by commas) into distinct categories. This ensured that each title could be accurately linked to multiple genres for more granular analysis.

## 3. Study Limitation and Scope

The analysis highlights that Netflix holds a disproportionately large share in the creation of original content. However, given the platform’s strategic reliance on original productions, simple volume comparisons with other studios would present an incomplete picture. To maintain clarity and focus, this project narrows its scope to two areas of particular interest: the animation genre and television series, allowing for a more balanced and meaningful exploration of trends.

![](Images/newplot(8).png)
![](Images/newplot(7)-imageonline.co-merged.png)

to see these charts yourslef click ![here1](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/pie_by_origin.html) , ![here2](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/pie_by_type.html), ![here3](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/pie_total_origin.html)

## 4. Deep Insight

Of course. Here is a professional analysis based on the two graphs provided, focusing on the production of animated content by each streaming service.

***

### Productions and Trends

![](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Images/newplot(12)-imageonline.co-merged.png)

This analysis reviews the production output of animated content across five major streaming platforms, examining both the internal focus of each service's library and their historical share of annual releases.

#### Internal Library Focus on Animation:
- The data reveals which platforms prioritize animation as a core part of their content library.
- Disney is the clear leader, dedicating the highest percentage of its total catalog to animation (approximately 5.7%). This aligns with its brand identity as a primary provider of animated features and series.
- HBO follows closely, with animation comprising about 5.0% of its library, indicating a significant strategic focus on the genre.
- Netflix (~3.9%) and Hulu (~3.6%) maintain a moderate, but smaller, focus on animation.
- Amazon Prime Video places the least emphasis on this genre, with animated titles making up less than 1% of its entire library.

#### Historical Production and Market Share Trends:
- The stacked bar chart illustrates how the market for new animated content has evolved over time.
- Early Market (Pre-2015): Netflix and Hulu were the dominant forces in streaming animation. Hulu, in particular, had a massive output spike around 2013, representing nearly 25% of the year's animated releases shown in the graph.
- Increased Competition (2016-2019): This period saw the landscape shift dramatically. While Netflix's output remained relatively steady, the entry and expansion of Disney and Amazon created a more competitive and fragmented market.
- Current Landscape (2020-Present): The market is now highly contested. 2020 was a peak year with significant releases from all major platforms. In the most recent years, Disney has emerged as a consistent and powerful force, frequently contributing the largest share of new animated content annually.

### **Conclusion**

In summary, a platform's internal focus on animation strongly correlates with its production activity. **Disney's** high library percentage is matched by its recent dominance in producing new animated titles. While early players like **Netflix and Hulu** established the market, they now face intense competition. **Amazon** remains a minor player, consistent with the low priority it gives the genre within its overall catalog.




### Ratings and Votes

![](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Images/newplot(16)-imageonline.co-merged.png)

![](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Images/newplot(16)-imageonline.co-merged(1).png)


This analysis synthesizes data from four charts comparing animated content on Amazon, Disney, HBO, Hulu, and Netflix based on ratings and viewer engagement.

#### Content Quality and Ratings:

- HBO consistently demonstrates the highest quality in its animated offerings. It leads all platforms with the highest average rating (approximately 7.8) and the highest weighted rating (approximately 7.4).

- Amazon Prime Video follows as a strong contender, securing the second-highest average rating.

- Disney, Hulu, and Netflix show more moderate performance, with their average and weighted ratings clustering around the 6.7 to 7.1 range, placing them in the lower tier for content quality among this group.

#### Audience Engagement and Popularity:

- There is a clear disconnect between content rating and audience engagement. Netflix is the dominant platform in terms of viewership, commanding the largest share of votes at 2.5%.

- Disney is the second most popular, with approximately 1.8% of the votes.

- In stark contrast to its high ratings, Amazon Prime Video has the lowest audience engagement, capturing less than 0.5% of the total votes. This suggests its catalog, while highly-rated, may be smaller or less viewed.

#### Historical Performance Trends (Weighted Rating Over Time):

- The quality of animated content has been highly volatile over the last decade. The line graph shows significant fluctuations for most services rather than stable year-over-year performance.

- Netflix exhibits the most dramatic changes, with a very high rating (around 8.5) before 2010, followed by a long period of fluctuation and a recent upward trend post-2022.

- Amazon, Disney, and HBO data is more recent but shows sharp peaks in quality within specific years (e.g., Amazon around 2019, Disney around 2024), indicating the impact of specific high-profile releases.

Conclusion

The data indicates that the platforms with the highest-rated animated content (HBO) are not the ones with the highest viewership (Netflix). Netflix's strategy appears to focus on a large volume of content that generates high engagement, even if the average quality is not top-tier. Conversely, services like HBO and Amazon seem to have a more curated, higher-quality selection that attracts a smaller but appreciative audience.
