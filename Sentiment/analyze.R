library(dplyr)
library(ggplot2)

# get files
files <- Sys.glob('data/*')

# for file 'x', read in and return sentiment values
extractSentiments <- function(x) {
  d <- read_delim(x, "\t", escape_double = FALSE,
                  col_names = FALSE, trim_ws = TRUE)
  d$X3
}

# create a list containing the sentiments from each file
s <- sapply(files, extractSentiments)
names(s) <- gsub('data/', '',names(s))
names(s) <- gsub('.txt', '',names(s))

# convert the list of sentiment values to a data frame
df <- NULL
for (i in 1:length(s)) {
  df <- rbind(df, data.frame(year = as.integer(names(s)[i]), sentiment = s[[i]]))
}

# look at the number of sentiment values (songs) for each year
counts <- df %>% group_by(year) %>% summarize(n = n())
ggplot(counts, aes(factor(year), n, fill = factor(year))) + geom_col() + 
  theme_classic() + xlab('year') +
  ggtitle('Number of sentiment values per year') +
  scale_x_discrete(breaks = seq(1960, 2020, by = 5)) +
  guides(fill = 'none')

# look at the sentiment for each year
ggplot(df, aes(factor(year), sentiment, fill = factor(year))) + geom_boxplot() + 
  geom_smooth(aes(group = 0)) + theme_classic() + xlab('year') +
  ggtitle('Sentiment of top songs by year') +
  scale_x_discrete(breaks = seq(1960, 2020, by = 5)) +
  guides(fill = 'none')








