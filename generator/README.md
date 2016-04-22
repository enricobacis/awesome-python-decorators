# turn functions into generators

  - `generator_of(size)`: This decorator factory turns the input into a
      generator (if it's not already so) chunking the input in pieces of the
      specified `size`. Then it processes each chunk and yields it as function
      output. This is useful when you want to create function that takes big
      inputs and do not clutter all your memory.

  - `generator`: This is the same as the one above but with a default chunk
      size of 4096 (which if the input is in bytes, it is one memory page).
