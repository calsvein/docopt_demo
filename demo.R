# author: Cal Schafer
# date: 2020-11-20

"This script prints out docopt args.
Usage: demo.R <arg1> --arg2=<arg2> [<arg2b>] [--arg3=<arg3>]
Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[<arg2b>]         Takes any value (this is an optional positional argument)
[--arg3=<arg3>]   Takes any value (this is an optional option)
" -> doc

library(docopt)

opt <- docopt(doc)

main <- function(arg1, arg2, arg3=NULL, arg4=NULL) {
  
    print(opt)
    print(typeof(opt))
    if (!is.null(opt$arg2b)) {
        print(opt$arg2b)  
    }
}

main(opt$arg1, opt$arg2, opt$arg3, opt$arg4)



