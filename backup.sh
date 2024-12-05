# Dump data base

current_date=$(date +"%Y-%m-%d")
echo $current_date
filename="pg.data.$current_date"
cd /docker/myfaculty/myfaculty
/usr/bin/docker compose exec -T -u postgres db pg_dump postgres > $filename
/usr/bin/rclone copy $filename gdrive:
rm $filename

tarfile="media.$current_date.tar.gz"
/usr/bin/tar czf $tarfile code/myfaculty/media
/usr/bin/rclone copy $tarfile gdrive:
rm $tarfile

 
