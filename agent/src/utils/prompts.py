recom_prompt="""
 You are assigned to create a recommendation based on the context :
  1-Look at the sensors data{sensor_readings}
  2-Look at the plots {plots}
  3-Generate recommendation
    """
anomaly_prompt="""
  You are assigned to check if there is a sensor anomaly based on the context:
  1-Look at the sensors data{sensor_readings}
  2-Look at the plots {plots}
  3-Look at the recommendation{recommendation}
  4-Check if there was a suspected anomaly {anomaly_suspected}
    """
