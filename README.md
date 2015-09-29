# SELinux Policy for  IBM TSM

Author: andreas@romab.com

As the IBM TSM client usually runs as root, unconfined, there are strong
reasons to confine it, mostly due to the default settings of letting the server
completely controll the client.

If you are installing this without using rpm, you must assign the following port 
types:

- tsmadmin_ssl_port_t
- tsm_ssl_port_t

## Examples

Shows port definitions:

    semanage port -l | grep tsm

Add admin port and backup port:

    semanage port -a -t tsmadmin_ssl_port_t -p tcp 1601
    semanage port -a -t tsm_ssl_port_t -p tcp 1600

## Booleans

Allows dsmc to traverse the filesystem and backup all data:    

    tsm_dsmc_can_backup_system (default on)
