from collections import deque

suggested_links = deque([int(el) for el in input().split()])
featured_links = [int(el) for el in input().split()]
target_engagement_value = int(input())
final_feed_collection = []

while suggested_links and featured_links:
    current_suggested_link = suggested_links.popleft()
    current_featured_link = featured_links.pop()

    bigger_link_sequence = ""
    remainder = 0

    if current_featured_link > current_suggested_link:
        bigger_link_sequence = "featured_links"
        remainder = current_featured_link % current_suggested_link
    elif current_featured_link < current_suggested_link:
        bigger_link_sequence = "suggested_links"
        remainder = current_suggested_link % current_featured_link
    else:
        final_feed_collection.append(0)

    if bigger_link_sequence == "featured_links":
        final_feed_collection.append(abs(remainder))
        if remainder != 0:
            remainder *= 2
            featured_links.append(remainder)
    elif bigger_link_sequence == "suggested_links":
        final_feed_collection.append(-abs(remainder))
        if remainder != 0:
            remainder *= 2
            suggested_links.append(remainder)

total_engament = sum(final_feed_collection)

print(f"Final Feed: {', '.join([str(x) for x in final_feed_collection])}")
if total_engament >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engament}")
else:
    print(f"Goal not achieved! Short by: {abs(target_engagement_value - total_engament)}")