movie_total_minutes = int(input("enter movie length: "))
print(movie_total_minutes)

# hours
hours = movie_total_minutes // 60
minutes = movie_total_minutes % 60
print(hours, ":", minutes)
