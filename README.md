# chunked-test

Demonstration of HTTP 1.1 chunked transfer encoding between Python and Javascript.
The Python server transmits content piece-meal. Meanwhile, the Javascript client 
receives intermediate progress events from the browser.
In a real application, this would be used to send data to the client as parts of it becomes available, rather than the server blocking until all content is available.
For example, an HTTP service that retrieved records from a database and generated JSON data from each could be implemented using a loop:
```
while (record = read_record(cursor)) {
  json = to_json(record);
  transmit_chunk(json);
}
```
This could be much more efficient than an implementation not using chunked encoding:
```
array_of_a_million_records = read_all_records(cursor);
array_of_a_million_json_blobs = to_json(array_of_a_million_records)
transmit(array_of_a_million_json_blobs);
```
Additionally, if each chunk were accompanied by an indication to the client of the progress of the operation, the client could inform the user of that progress, for example using a progress bar. This would be superior to the usual user experience, involving a message from the browser that a response is being read, but no other visible sign that progress is being made, resulting in a perception by users that the operation is 'stuck'.
