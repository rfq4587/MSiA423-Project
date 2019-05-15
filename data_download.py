import boto3
import argparse


def main(args):
    s3 = boto3.resource(args.aws_resource, aws_access_key_id='AKIAJ7IO2WG3EEVXNHUA', aws_secret_access_key='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')
    bucket = s3.Bucket(args.bucket_name)
    bucket.download_file(args.filepath, args.outfilename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--aws_resource', type=str, default='s3' , help='AWS data resource (default=s3)')
    parser.add_argument('--bucket_name', type=str, default='nw-henry-s3' , help='Resouce bucket name (default=nw-henry-s3)')
    parser.add_argument('--filepath', type=str, default='data/h1b.csv', help='The location of the file in the bucket (default=data/h1b.csv)')
    parser.add_argument('--outfilename', type=str, default='h1b.csv', help='Output location of the file (default=h1b.csv)')

    args = parser.parse_args()
    print(args)
    main(args)
