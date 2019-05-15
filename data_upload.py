import boto3
import argparse


def main(args):
    s3 = boto3.resource(args.aws_resource)
    bucket = s3.Bucket(args.bucket_name)
    bucket.upload_file(args.filepath, args.outputname)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--aws_resource', type=str, default='s3' , help='AWS data resource (default=s3)')
    parser.add_argument('--bucket_name', type=str, default='nw-henry-s3' , help='Resouce bucket name (default=nw-henry-s3)')
    parser.add_argument('--filepath', type=str, default='./h1b.csv', help='The location of the file in the local (default=./h1b.csv)')
    parser.add_argument('--outputname', type=str, default='h1b.csv', help='Output name of the file (default=h1b.csv)')

    args = parser.parse_args()
    print(args)
    main(args)
