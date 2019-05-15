#library

library(ggplot2)
library(maps)
library(ggridges)
library(dplyr)
library(ggthemes)
library(extrafont)

# league five with average and relative curves, average league consumption per player
# Expend_by_player

liga_petice <- read.csv("/home/kristijan/github/FootballEvolcion/Datas/SaveData/save_csv_Expend_BATCH.csv")
colnames(liga_petice) <- c("Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION")

gr <- ggplot(liga_petice,aes(x = Year, y = Expend_by_player , col = Name_of_Legue)) +
  geom_line(alpha = 0.9) +
  geom_smooth(lwd = 2, se = FALSE) +
  scale_y_continuous("Average Expend  per player",labels = scales::comma) +
  scale_colour_manual(values = c("gray15", "orange4", "cyan4","darkolivegreen","red4")) +
  labs(title = "Average League player consumption per player",color = " Names of Leagues\n")

gr + theme_tufte() +
  theme(
    legend.position = c(0.7, 0.9),
    legend.title = element_text(face = "bold", size = 12),)

gr +theme( axis.title=element_text(size=17,face="bold"),
           axis.text = element_text(face = "bold", size = 17),
           plot.title = element_text(size = 20, face = "italic",color = "red"))
