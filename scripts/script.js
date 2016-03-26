$(document).ready(function() {
	campus_key = {
		'umich': 'University of Michigan - Ann Arbor',
		'penn': 'University of Pennsylvania',
		'harvard': 'Harvard University',
		'cal': 'University of California at Berkeley',
		'umass': 'University of Massachusetts - Amherst',
		'vt': 'Virginia Tech',
		'unc': 'University of North Carolina - Chapel Hill',
		'uw': 'University of Washington',
		'utt': 'University of Texas - Austin',
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
		'waterloo': 'University of Waterloo',
		'wisconsin': 'University of Wisconsin'
	}
	$('#panel').click(function() {
		$('.from-right').addClass('is-visible')
	})
	$(".schoolbutton").click(function() {
		$('.campus-title').remove();
		$('#campus').prepend("<h3 class='campus-title'>" + campus_key[$(this).attr('id')] + "</h3>");
	})

})