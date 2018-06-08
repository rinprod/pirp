#!/usr/bin/env Rscript

# define the repo to use later
REPO <- "https://cloud.r-project.org/"

# Get any command line args
args <- commandArgs(trailingOnly = TRUE)

# Check that there is at least one arg specified
if ( is.na(args[1]) ){
  stop("No input file or package name(s) specified")
}

# Check if the specified file exists
if ( file.exists(args[1]) ) {
  # read the file into a vector
  packages <- readLines(args[1])
  
  # Install the packages
  install.packages(packages[packages != ""], repos = REPO)
} else {
  install.packages(args, repos = REPO)
}
