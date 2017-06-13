## Amazon Cookbook
### Information about Regions and Availability Zones
* https://aws.amazon.com/about-aws/global-infrastructure/
* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
* http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html
* https://aws.amazon.com/ec2/instance-types/

### Create a disk and attach it to your VM
    ```$ aws configure
    $ aws ec2 create-volume --size 80 --region us-east-1 --availability-zone us-east-1b --volume-type gp2
    $ aws ec2 attach-volume --volume-id vol-0c16975a46525c1ab --instance-id i-0a086d942418646d2 --device xvdb
    $ lsblk
    $ sudo mkfs.ext4 /dev/xvdb
    $ sudo mount /dev/xvdb /mnt
    ```
References:
* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html
* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html
* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html
* http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-expand-volume.html
* http://docs.aws.amazon.com/cli/latest/reference/ec2/attach-volume.html
* http://docs.aws.amazon.com/cli/latest/reference/ec2/create-volume.html

### Information about running instances

References:
* http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html
* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

## Python Style
* Indent with 4 spaces.

* Do not use tabs. If you can, configure your editor to expand tabs to spaces. This is useful because different editors have tab stops set at different positions.  If you are using EMACS, you can specify this by adding this to you .emacs file:

```(setq-default indent-tabs-mode nil)
(setq c-basic-offset 4)```

For further information on why tabs are a bad idea, see:

** [http://www.emacswiki.org/emacs/NoTabs](http://www.emacswiki.org/emacs/NoTabs)
** [http://www.jwz.org/doc/tabs-vs-spaces.html](http://www.jwz.org/doc/tabs-vs-spaces.html)
** [http://slashdot.org/pollBooth.pl?qid=395&aid=-1](http://slashdot.org/pollBooth.pl?qid=395&aid=-1)

