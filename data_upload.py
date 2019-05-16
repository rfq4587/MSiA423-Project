import boto3
import argparse


def main(args):
    s3 = boto3.resource(args.aws_resource, aws_access_key_id=args.aws_access_id, aws_secret_access_key=args.aws_secret_access_key)
    bucket = s3.Bucket(args.bucket_name)
    bucket.upload_file(args.filepath, args.outputname)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--aws_access_id', type=str, help='aws_access_id')
    parser.add_argument('--aws_secret_access_key', type=str, help='aws_secret_access_key')
    parser.add_argument('--aws_resource', type=str, default='s3' , help='AWS data resource (default=s3)')
    parser.add_argument('--bucket_name', type=str, default='nw-henry-s3' , help='Resouce bucket name (default=nw-henry-s3)')
    parser.add_argument('--filepath', type=str, default='./h1b.csv', help='The location of the file in the local (default=./h1b.csv)')
    parser.add_argument('--outputname', type=str, default='uploaded.csv', help='Output name of the file (default=uploaded.csv)')

    args = parser.parse_args()
    print(args)
    main(args)
