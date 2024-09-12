def format_date(date_str):
   month_mapping = {
      'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
      'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
      'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
   }
   parts = date_str.split()
   day = parts[2].zfill(2)
   month = month_mapping[parts[1][:3]]
   year = parts[3]
   return f"{year}-{month}-{day}"