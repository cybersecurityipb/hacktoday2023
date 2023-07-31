## yesterday-afternoon-kidz
- MITM proxy
- SQL injection Log Analysis

## Desc
Our live proxy has detected hacking activity in our logs; analyze the log file to find out what data the hacker retrieved

## Solution
You can visualize it in Mitmweb and observe that someone is attempting to inject SQL injection. The query submits successfully every one second or generates errors in the responses. Additionally, you can create a script using the Mitmproxy Python library to see the data stream.



## Flag
`hacktoday{it-yesterday_database_secret_sorry_i_need_to_make_this_long_enough_for_manual_player_like_yesterday_afternoon_kidz_or_it_will_be_too_damn_sleepy(1)_right?}`
