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


def sorted_logs(log_entries):
   most_recent_logs = {}

   for log_batch in log_entries:
      for service_name, log_data in log_batch.items():
         formatted_date = format_date(log_data['date'])
         log_timestamp = f"{formatted_date} {log_data['time']}"

         if service_name not in most_recent_logs or log_timestamp > most_recent_logs[service_name]['timestamp']:
               most_recent_logs[service_name] = {
                  'service_name': service_name,
                  'log_type': log_data['log_type'],
                  'date': formatted_date,
                  'time': log_data['time'],
                  'timestamp': log_timestamp
               }

   consolidated_logs = [log_info for log_info in most_recent_logs.values()]
   consolidated_logs.sort(key=lambda x: x['timestamp'], reverse=True)

   final_output = [
      {
         'date': log['date'],
         'time': log['time'],
         'service_name': log['service_name'],
         'log_type': log['log_type']
      }
      for log in consolidated_logs
   ]

   return final_output

