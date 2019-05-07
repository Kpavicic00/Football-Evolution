library(ggplot2)

dataF <- read.csv("/home/kristijan/github/FootballEvolcion/Datas/SaveData/save_csv_GetBYyear.csv") #citanje iz filea

colnames(dataF) <- c("Order","Year", "Expend", "Income","Income","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas",
"avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season ")


dataF$Order <- as.factor(dataF$Order)
dataF$Year <- as.factor(dataF$Year)
dataF$Expend <- as.factor(dataF$Expend)
dataF$Income <- as.factor(dataF$Income)
dataF$number_of_Season <- as.factor(dataF$number_of_Season)
dataF$sum_of_Arrivlas <- as.factor(dataF$sum_of_Arrivlas)
dataF$sum_of_Depatrues <- as.factor(dataF$sum_of_Depatrues)
dataF$avg_Expend_of_Arrivlas <- as.factor(dataF$avg_Expend_of_Arrivlas)
dataF$avg_Income_of_Depatrues <- as.factor(dataF$avg_Income_of_Depatrues)
dataF$avg_Expend_Season <- as.factor(dataF$avg_Expend_Season)
dataF$avg_Income_Season <- as.factor(dataF$avg_Income_Season)
dataF$avg_Balance_Season <- as.factor(dataF$avg_Balance_Season)

ggplot(dataF, aes(x = dataF$Expend, fill = Expenditure ))+
  theme_bw() +
  geom_bar() +
  labs(y = "counter", title = "potrosnja")
#prop.table(table(dataF$sum_of_Arrivla))
