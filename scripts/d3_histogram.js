//campus key
campus_key = {
    'umich': 'University of Michigan - Ann Arbor',
    'penn': 'University of Pennsylvania',
    'harvard': 'Harvard University',
    'cal': 'University of California at Berkeley',
    'umass': 'University of Massachusetts - Amherst',
    'vt': 'Virginia Tech',
    'unc': 'University of North Carolina - Chapel Hill',
    'uw': 'University of Washington',
    // 'utt': 'University of Texas - Austin',
    'usc': 'University of Southern California',
    'ucla': 'University of California - Los Angeles',
    'ucsd': 'University of California - San Diego',
    'ill': 'University of Illinois - Urbana-Champaign',
    'purdue': 'Purdue University',
    'princeton': 'Princeton University',
    'mit': 'Massachusetts Institute of Technology',
    'harveymudd': 'Harvey Mudd College',
    'stanford': 'Stanford University',
    'carnegie': 'Carnegie Mellon University',
    'columbia': 'Columbia University',
    'cornell': 'Cornell University',
    'gt': 'Georgia Institute of Technology',
    'rice': 'Rice University',
    'rensselaer': 'Rensselaer Polytechnic Institute',
    'brown': 'Brown University',
    'caltech': 'California Institute of Technology',
    'cp': 'California Polytechnic State University',
    'maryland': 'University of Maryland - College Park',
    'waterloo': 'University of Waterloo'
    // 'wisconsin': 'University of Wisconsin'
  } 

//Beginning of d3 code
  var hist_margin = {top: 25, right: 20, bottom: 80, left: 150},
      hist_width = 765 - hist_margin.left - hist_margin.right,
      hist_height = 300 - hist_margin.top - hist_margin.bottom;
      padding = -150;

  var x = d3.scale.ordinal()
      .rangeRoundBands([0, hist_width], .1);

  var y = d3.scale.linear()
      .range([hist_height, 0]);

  var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");

  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left")
      .ticks(10);

  var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<span style='color:yellow'>" + " " + d[a] + "</span><strong> Reviews: </strong> <span style='color:lightblue'>" + Math.round(d[b])+ "</span>";
  })

  var svg = d3.select(".histogram-campus").append("svg")
      .attr("width", hist_width + hist_margin.left + hist_margin.right)
      .attr("height", hist_height + hist_margin.top + hist_margin.bottom)
      .append("g")
      .attr("transform", "translate(" + hist_margin.left + "," + hist_margin.top + ")");      

  $('.histogram-campus svg').attr("style", "padding-left:150px;")
  update('cal');

  svg.call(tip);

function update(data_in) {

d3.tsv("../209_FinalProject_Data/campus_histogram_data.tsv", function(error, data) {

   a = data_in;
   b = data_in + "_" + "count"; //Review Count
   
  
   //This code needs to be lined up with the naming above to work properly
   data.forEach(function(d) {
    d[b] = +d[b]; 
    });

  x.domain(data.map(function(d) { return d[a]; }));
  y.domain([0, d3.max(data, function(d) { return d[b]; })]);  //Setting range for y

  svg = d3.select(".histogram-campus").selectAll("svg");
  
    var trans = d3.select(".histogram-campus").transition().duration(200);
        delay = function(d, i) { return i * 5; };
      
      var rect = svg.selectAll(".bar")
                    .data(data);


           //re-append chart with new data         
          rect.enter().append("rect")

          rect
             .attr("class", "bar")
             .on('mouseover', tip.show)
             .on('mouseout', tip.hide)
             .attr("x", function(d) { return x(d[a]); })
             .attr("width", x.rangeBand())
             .attr("y", function(d) { return y(d[b]); })
             .transition()
             .delay(function(d, i) { return i * 100; })
             .duration(200)
             .attr("height", function(d) { return hist_height - y(d[b]); });
              //.duration(850)
              //.delay(delay);   //- y(d[b]

 svg.select(".x.axis").remove(); //Remove previous x axis

 svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + hist_height + ")")
    .call(xAxis)
    .selectAll("text")
    .style("text-anchor", "middle")
    .attr("dx", "2.2em")
    .attr("dy", "1.15em")
    .attr("transform", "rotate(25)" );     


 svg.select(".y.axis").remove(); //Remove previous y-axis

 svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)  
    .append("text")
    .attr("transform", "translate("+ (padding/2) +","+(hist_height/2)+")rotate(-90)")
    .attr("y", 10)
    .attr("dy", ".90em")
    .style("font-size", "16px")
    .style("text-anchor", "end")
    .text("Average Reviews ");


//remove existing image when doing the transition
rect.exit().transition().remove();   

  });
}