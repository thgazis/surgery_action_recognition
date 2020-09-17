for file in data/annotated_data/knot_tying/avi2/*; 
  do name=`echo "$i`
  echo "$file"
  f="$(basename -- $file)"
  ffmpeg -i "$file" -vf scale=224:224,fps=fps=5 "data/preprocessed_data/knot_tying/${file##*/}.avi"
done