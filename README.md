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
The dataset was compiled from IMDb based on original productions from Netflix, Hulu, Amazon, Disney, and HBO. After appending and cleaning the CSV files, the data was imported into MySQL for structured analysis. The 'everything.csv' file contains 4000+ records for all the produced media. The 'genres.csv' contain 12000+ records when those media titiles are split according to their genres. 

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

To use these plots ![click here](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/genre_comparison_by_origin.html) and ![here](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/genre_trends_by_year.html)

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


### Ratings and Votes

![](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Images/newplot(16)-imageonline.co-merged.png)

![](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Images/newplot(16)-imageonline.co-merged(1).png)

To use these plots ![clicke here1](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/weighted_rating_bar.html), ![here2](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/votes_percentage_by_origin.html), ![here3](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/weighted_rating_by_origin.html), ![here4](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/weighted_rating_trends.html)

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


### Cancellation Trends 

![](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Images/newplot(21)-imageonline.co-merged.png)
![](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Images/newplot(20)-imageonline.co-merged.png)

To use these plots click ![here1](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/avg_rating_bar.html), ![here2](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/status_percentage_by_rating.html), ![here3](https://github.com/Vishal-Deb/The-Trends-in-Original-Media/blob/main/Generated%20Plots/weighted_rating_bar.html).

This analysis examines how streaming services decide whether to cancel an animated TV show or allow it to reach a natural conclusion, based on the show's rating. The data reveals starkly different strategies between platforms. Here the percentage of shows cancelled/concluded compared to shows produced in the genre is provided. 

#### Cancellation Strategies and Quality Threshold:

- HBO exhibits the most stringent quality control. The average weighted rating of an animated show it cancels is remarkably high at approximately 7.6. Furthermore, 100% of its cancellations fall within the high 7-9 rating range, indicating it will cancel even high-performing shows that don't meet its elite standards.

- Netflix follows a more conventional strategy. It cancels the lowest-rated shows on average (around 6.9). A significant majority (over 60%) of its cancelled shows are rated below 6.0, suggesting that poor performance is the primary driver for cancellation.

- Disney and Hulu fall in the middle, cancelling shows with an average rating of about 7.1. Their cancellations are concentrated in the mid-tier 6-8 rating range.

#### Conclusion Strategies (Which Shows Get a Proper Ending):

- Amazon Prime Video prioritizes giving its best-rated shows a definitive conclusion. The average rating of its concluded animated shows is the highest of all platforms (approximately 7.4), and 100% of these shows are rated 7.0 or higher.

- Disney and Hulu show a peculiar and opposite trend. For both platforms, 100% of the animated shows that have reached a conclusion are rated below 7.0. This suggests a strategy where higher-rated, successful animated shows are kept running or left open-ended, while only lower-rated series are given a final season.

- Netflix and HBO allow shows to conclude across a wider spectrum of quality, with a mix of concluded shows in the 6-7, 7-8, and 8-9 rating brackets.

#### Important Disclaimer

- Data Collection and Accuracy: Please be aware that the data for this study was collected using AI and automated methods. As such, there is a possibility of errors or inaccuracies within the dataset.

- Limitations of Analysis: This analysis identifies trends and correlations between show ratings and their cancellation or conclusion. However, it cannot determine the true, multi-faceted reasoning behind a studio's decision. The cancellation of a show is a complex business decision influenced by many factors beyond public ratings, such as production costs, specific viewership metrics, licensing agreements, and shifts in strategic direction.



### 5. Conclusion

Based on a holistic review of the data—covering production volume, content quality, audience engagement, and series lifecycle management—it is clear that each major streaming platform employs a distinct and consistent strategy for its animated content. There is no single path to success; rather, each service has tailored its approach to fit its overarching brand identity and business model.

- HBO: The Prestige Curator

  - Strategy: HBO treats animation as a prestige genre, dedicating a significant portion of its library to it and achieving the highest average quality ratings. Its focus is on critical acclaim over mass-market appeal.

  - Lifecycle: Its curation is ruthless. HBO maintains its elite standard by cancelling even high-rated shows that don't meet its exceptional bar, demonstrating a "quality-over-quantity" philosophy.

- Netflix: The Volume and Engagement Leader

  - Strategy: Netflix’s model is built on market saturation. While its average quality is moderate, it dominates in production volume and audience engagement, capturing the largest share of viewers.

  - Lifecycle: Its approach is pragmatic and data-driven. The platform systematically prunes its lowest-rated, underperforming content while allowing a wide variety of other shows to play out, optimizing its vast and diverse catalog for broad appeal.

- Disney+: The Brand Champion

  - Strategy: Animation is the core of Disney's brand identity. It dedicates the highest percentage of its library to the genre and has become a dominant force in producing new animated content.

  - Lifecycle: Its management strategy is protective of its intellectual property. High-rated, successful shows are treated as long-term assets and are rarely given definitive conclusions, ensuring the longevity of valuable franchises. Meanwhile, lower-rated shows are allowed to conclude.

- Amazon Prime Video: The Niche Quality Provider

  - Strategy: Amazon is a minor but deliberate player in animation, with the smallest library share and lowest audience engagement. Its focus appears to be on targeted, high-quality acquisitions or productions.

  - Lifecycle: It invests in its content's integrity. Amazon shows a strong tendency to allow its high-rated animated series to reach a proper, planned conclusion, rewarding the niche audience it attracts for that content.

- Hulu: The Legacy Competitor

  - Strategy: As an early market player, Hulu maintains a moderate focus on animation but now faces intense competition.

  - Lifecycle: Its content strategy appears aligned with its partner, Disney. It avoids concluding its successful, higher-rated animated series, likely to retain viewership and keep valuable assets in play.
 
### 6. Recommendations for Future Application

This comprehensive analysis of streaming platform strategies provides actionable intelligence for various stakeholders. The insights can be used to inform decision-making, from creative development to investment strategy.

#### For Content Creators and Animation Studios:

- Strategic Pitching: Creators can tailor their pitches to align with a platform's demonstrated strategy. High-concept, prestige projects are best suited for HBO, while shows with broad engagement potential and franchise possibilities are ideal for Netflix and Disney+.

- Narrative Planning: For series with a definitive, planned story arc, Amazon Prime Video appears to be the most receptive home. Conversely, pitches to Disney+ or Hulu should emphasize a concept's potential for longevity and open-ended storytelling.

- Risk Assessment: Understanding a platform's cancellation habits is crucial. A high-rated show on HBO is not guaranteed safety, whereas a moderately-rated show on Netflix that avoids the lowest performance tier has a better chance of survival.

#### For Investors and Market Analysts:

- Evaluating Business Models: The analysis provides a clear framework for comparing the viability of different streaming strategies. Investors can contrast the high-cost, high-prestige model of HBO against the volume-driven, mass-market model of Netflix to assess long-term profitability and market sustainability.

- Identifying Growth and Risk: Amazon's minimal footprint in animation signals a potential area for future growth or a persistent strategic weakness. Similarly, Disney's increasing dominance in production volume could signal a risk of market monopolization, affecting smaller players.

- Predicting Content Cycles: The data reveals predictable patterns, such as Netflix's tendency to cancel low-rated shows. This can be used to forecast content churn and evaluate the stability of a platform's library.

#### For Consumers:

- Informed Subscription Choices: Viewers can select services that best align with their tastes. A consumer seeking critically acclaimed masterpieces would gravitate towards HBO, while one wanting the largest variety would choose Netflix. Families and fans of long-running universes would find the most value in Disney+.

- Managing Expectations: By understanding that platforms like Disney+ and Hulu often keep their highest-rated shows open-ended, viewers can adjust their expectations regarding series conclusions. Conversely, viewers seeking satisfying, complete narratives may find them more consistently on Amazon Prime Video.
