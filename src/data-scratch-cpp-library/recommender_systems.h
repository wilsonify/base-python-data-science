import math
from collections import defaultdict, Counter

from dsl.linear_algebra import dot



double most_popular_new_interests(user_interests, max_results=5) ;

//
// user-based filtering
//


double cosine_similarity(v, w) ;

double make_user_interest_vector(user_interests) ;

double most_similar_users_to(user_id) ;

double user_based_suggestions(user_id, include_current_interests=False) ;
//
// Item-Based Collaborative Filtering
//


double most_similar_interests_to(interest_id) ;

double item_based_suggestions(user_id, include_current_interests=False) ;