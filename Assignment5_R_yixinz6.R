# Set dataset location
getwd()
setwd('C:\\Users\\irenezyx\\Documents\\IS 590 DV\\HW5')

# Read from csv
df <- read.csv("IL_Building_Inventory.csv", header=TRUE)

# Set NAN values to be 0
df$Year.Constructed[is.na(df$Year.Constructed)] <- 0
df$Year.Acquired[is.na(df$Year.Acquired)] <- 0

# Plot scatters
plot(df$Year.Acquired, df$Year.Constructed, col="blue")

library(shiny)

plotOutput("plot1", click = "plot_click")

ui <- basicPage(
  plotOutput("plot1", click = "plot_click"),
  verbatimTextOutput("info")
)

server <- function(input, output) {
  output$plot1 <- renderPlot({
    plot(df$Year.Acquired, df$Year.Constructed, col="blue")
  })

  output$info <- renderText({
    paste0("x=", input$plot_click$x, "\ny=", input$plot_click$y)
  })
}

shinyApp(ui, server)




