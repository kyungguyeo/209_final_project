//Beginning of d3 code, set up SVG
var businessmargin = {top: 20, right: 10, bottom: 50, left: 150},
    businesswidth = 750 - businessmargin.left - businessmargin.right,
    businessheight = 325 - businessmargin.top - businessmargin.bottom;
    businesspadding = -150;

var businessx = d3.scale.ordinal()
    .rangeRoundBands([0, businesswidth], .1);


var businessy = d3.scale.linear()
    .range([businessheight, 0]);

var businessxAxis = d3.svg.axis()
    .scale(businessx)
    .orient("bottom")
    .tickPadding(5);


var business_histogram_svg = d3.select(".histogram-business").append("svg")
    .attr("width", businesswidth + businessmargin.left + businessmargin.right)
    .attr("height", businessheight + businessmargin.top + businessmargin.bottom)
    .append("g")
    .attr("transform", "translate(" + businessmargin.left + "," + businessmargin.top + ")");    

businessupdate('DO1Ukiuia9hs33VTnTY_Jg')  //Initial output when user first launch the site

//Take in school id and update the data then histogram based on the id
function businessupdate(data_in) {

d3.tsv("../209_FinalProject_Data/histogram_business.tsv", function(error, data) {
  
   a = 'reviews';
   b = data_in; //Review Count
   
   c = d3.max(data, function(d) { return d[b]; } )

   var businessyAxis = d3.svg.axis()
    .scale(businessy)
    .orient("left")
    .ticks(c); 
  
   //This code needs to be line up with the naming above to work properly
   //SRC="/Users/Maximus/Desktop/W209_DB/Final Project/images.png"></a>
   data.forEach(function(d) {
    d[b] = +d[b]; 
    });
  
  businessx.domain(data.map(function(d) { return d[a]; }));
  businessy.domain([0, d3.max(data, function(d) { return d[b]; })]);  //Setting range for y

  
    var trans = d3.select(".histogram-business").transition().duration(200);
        delay = function(d, i) { return i * 5; };
      var rect = business_histogram_svg.selectAll(".business-bar")
                    .data(data);

           //re-append chart with new data         
          rect.enter().append("rect")

          rect
             .attr("class", "business-bar")
             .attr("x", function(d) { return businessx(d[a]); })
             .attr("width", businessx.rangeBand())
             .attr("y", function(d) { return businessy(d[b]); })
             .transition()
             .delay(function(d, i) { return i * 100; })
             .duration(200)
             .attr("height", function(d) { return businessheight - businessy(d[b]); });

 business_histogram_svg.select(".business-x axis").remove(); //Remove previous x axis

 business_histogram_svg.append("g")
    .attr("class", "business-x axis")
    .attr("transform", "translate(0," + (businessheight)  + ")")
    .call(businessxAxis);
    
  business_histogram_svg.append("text")
    .attr("transform", "translate("+ (businesswidth/2) +","+(businessheight + 37)+")")  // centre below axis
    .style("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
    .text("Stars");    


 business_histogram_svg.select(".business-y axis").remove(); //Remove previous y-axis

 business_histogram_svg.append("g")
    .attr("class", "business-y axis")
    .call(businessyAxis)  
    .append("text")
    .attr("transform", "translate("+ (businesspadding/2) +","+(businessheight/2)+")rotate(-90)")
    .attr("y", 15)
    .attr("dy", "0.1em")
    .style("font-size", "20px")
    .style("text-anchor", "middle")
    .text("# Reviews");


//remove existing image when doing the transition
rect.exit().transition().remove();   

  });
}