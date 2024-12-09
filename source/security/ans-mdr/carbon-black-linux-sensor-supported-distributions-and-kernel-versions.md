```eval_rst
   .. title:: Carbon Black Linux Sensor Supported Distributions and Kernel Versions
   .. meta::
      :title: Carbon Black Linux Sensor Supported Distributions and Kernel Versions | ANS Documentation
      :description: How to prevent Logjam attacks based on weak Diffie-Hellman key exchange
      :keywords:  logjam, SSL, TLS, attack, attacks, log, jam, deffie hellman
```

<style>
    .sensor-table {
        width: 100%;
    }

    .sensor-table th {
        background-color: #e3e8ef;
        color: #202e52;
        border-bottom: 0;
    }

    .sensor-table td {
        border-bottom: 0;
        color: #202e52;
    }

    .sensor-table tbody tr:nth-child(even) td {
        background-color: #f8fafc;
    }

    .sensor-table td.not-supported {
        font-weight: bold;
    }
</style>

# Carbon Black Linux Sensor Supported Distributions and Kernel Versions

Please refer to the below compatibility matrix for supported Linux operating systems and kernels before purchase and
installation.

## Operating Systems

* [RHEL](#rhel)
* [CentOS](#centos)
* [SUSE](#suse)
* [OpenSUSE](#opensuse)
* [Amazon Linux](#amazon-linux)
* [Debian](#debian)
* [Ubuntu](#ubuntu)
* [Oracle](#oracle)
* [AlmaLinux](#almalinux)
* [Rocky Linux](#rocky-linux)

## RHEL

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>9.3</td>
            <td>5.14.0-362</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>9.2</td>
            <td>5.14.0-284.11.1</td>
            <td>2.15.0-2.16.0</td>
            <td>2.15.0-2.16.0</td>
        </tr>
        <tr>
            <td>9.1</td>
            <td>5.14.0-162</td>
            <td>2.14.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>9.0</td>
            <td>5.14.0-70</td>
            <td>2.14.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.10</td>
            <td>4.18.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>8.9</td>
            <td>4.18.0-513.5.1</td>
            <td>2.15.2-2.16.0</td>
            <td>2.15.2-2.16.0</td>
        </tr>
        <tr>
            <td>8.8</td>
            <td>4.18.0-477.10.1</td>
            <td>2.15.0-2.16.0</td>
            <td>2.15.0-2.16.0</td>
        </tr>
        <tr>
            <td>8.7</td>
            <td>4.18.0-425</td>
            <td>2.14.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.6</td>
            <td>4.18.0-372</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.5</td>
            <td>4.18.0-348</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.4</td>
            <td>4.18.0-305</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.3</td>
            <td>4.18.0-240</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.2</td>
            <td>4.18.0-193</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.1</td>
            <td>4.18.0-147</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.0</td>
            <td>4.18.0-80</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.9</td>
            <td>3.10.0-1160</td>
            <td>2.9.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.8</td>
            <td>3.10.0-1127</td>
            <td>2.7.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.7</td>
            <td>3.10.0-1062</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.6</td>
            <td>3.10.0-957</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.5</td>
            <td>3.10.0-862</td>
            <td>2.7.0-2.16.0</td>
             <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.4</td>
            <td>3.10.0-693</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.3</td>
            <td>3.10.0-514</td>
            <td>2.7.0-2.16.0</td>
             <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.2</td>
            <td>3.10.0-327</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.1</td>
            <td>3.10.0-229</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.0</td>
            <td>3.10.0-123</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.10</td>
            <td>2.6.32-754</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.9</td>
            <td>2.6.32-696</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.8</td>
            <td>2.6.32-642</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.7</td>
            <td>2.6.32-573</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.6</td>
            <td>2.6.32-504</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
    </tbody>
</table>

## CentOS

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8.5</td>
            <td>4.18.0-348</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.4</td>
            <td>4.18.0-305</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.3</td>
            <td>4.18.0-240</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.2</td>
            <td>4.18.0-193</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.1</td>
            <td>4.18.0-147</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.0</td>
            <td>4.18.0-80</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.9</td>
            <td>3.10.0-1160</td>
            <td>2.9.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.8</td>
            <td>3.10.0-1127</td>
            <td>2.7.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.7</td>
            <td>3.10.0-1062</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.6</td>
            <td>3.10.0-957</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.5</td>
            <td>3.10.0-862</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.4</td>
            <td>3.10.0-693</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.3</td>
            <td>3.10.0-514</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.2</td>
            <td>3.10.0-327</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.1</td>
            <td>3.10.0-229</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.0</td>
            <td>3.10.0-123</td>
            <td>2.7.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.10</td>
            <td>2.6.32-754</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.9</td>
            <td>2.6.32-696</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.8</td>
            <td>2.6.32-642</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.7</td>
            <td>2.6.32-573</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.6</td>
            <td>2.6.32-504</td>
            <td>2.7.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
    </tbody>
</table>

## SUSE

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>15 SP6</td>
            <td>6.4.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>15 SP5</td>
            <td>5.14.21</td>
            <td>2.15.1-2.16.0</td>
            <td>2.15.1-2.16.0</td>
        </tr>
        <tr>
            <td>15 SP4</td>
            <td>5.14.21-150400</td>
            <td>2.14.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>15 SP3</td>
            <td>5.03.18-57</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>15 SP2</td>
            <td>5.03.18-22</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>15 SP1</td>
            <td>4.12.14-195</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>15</td>
            <td>4.12.14-23</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>12.5</td>
            <td>4.12.14-120</td>
            <td>2.11.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>12.4</td>
            <td>4.12.14-94</td>
            <td>2.11.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>12.3</td>
            <td>4.04.73-5</td>
            <td>2.11.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>12.2</td>
            <td>4.04.21-69</td>
            <td>2.11.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
    </tbody>
</table>

## OpenSUSE

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>15.6</td>
            <td>6.4.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>15.5</td>
            <td>5.14.21</td>
            <td>2.15.1-2.16.0</td>
            <td>2.15.1-2.16.0</td>
        </tr>
        <tr>
            <td>15.4</td>
            <td>5.14.21</td>
            <td>2.14.0-2.16.0</td>
            <td>2.15.1-2.16.0</td>
        </tr>
        <tr>
            <td>15.3</td>
            <td>5.3.18</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>15.2</td>
            <td>5.3.18</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>15.1</td>
            <td>4.12.14</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>15.0</td>
            <td>4.12.14</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>42.2</td>
            <td>4.4.21</td>
            <td>2.11.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>42.3</td>
            <td>4.4.73</td>
            <td>2.11.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
    </tbody>
</table>

## Amazon Linux

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2023</td>
            <td>6.1.15</td>
            <td>2.15.0-2.16.0</td>
            <td>2.15.0-2.16.0</td>
        </tr>
        <tr>
            <td>2</td>
            <td>5.10.177-158.645</td>
            <td>2.15.1-2.16.0</td>
            <td>2.15.1-2.16.0</td>
        </tr>
        <tr>
            <td></td>
            <td>4.14</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
    </tbody>
</table>

## Debian

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12.5</td>
            <td>6.1.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>12.0-12.2</td>
            <td>6.1.0</td>
            <td>2.15.1-2.16.0</td>
            <td>2.15.1-2.16.0</td>
        </tr>
        <tr>
            <td>11.9</td>
            <td>5.10.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>11.8</td>
            <td>5.10.0</td>
            <td>2.15.2-2.16.0</td>
            <td>2.15.2-2.16.0</td>
        </tr>
        <tr>
            <td>11.7</td>
            <td>5.10.0</td>
            <td>2.15.2-2.16.0</td>
            <td>2.15.2-2.16.0</td>
        </tr>
        <tr>
            <td>11.1-11.6</td>
            <td>5.3.18</td>
            <td>2.14.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>10.10-10.11, 10.13</td>
            <td>4.19</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>10.0-10.09</td>
            <td>4.19</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>9.0-9.13</td>
            <td>4.9</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
    </tbody>
</table>

## Ubuntu

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>22.10</td>
            <td>5.19.0</td>
            <td>2.14.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>22.04.4</td>
            <td>5.15</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>22.04.3</td>
            <td>6.5</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>22.04.3</td>
            <td>5.15</td>
            <td>2.15.2</td>
            <td>2.15.2</td>
        </tr>
        <tr>
            <td>22.04</td>
            <td>5.15</td>
            <td>2.14.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>21.10</td>
            <td>5.13</td>
            <td>2.11.3-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>21.04</td>
            <td>5.11</td>
            <td>2.11.3-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>20.04</td>
            <td>5.4</td>
            <td>2.11.0-2.16.0</td>
            <td>2.14.1-2.16.0</td>
        </tr>
        <tr>
            <td>19.10</td>
            <td>5.3</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>19.04</td>
            <td>5.0</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>18.10</td>
            <td>4.18</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>18.04</td>
            <td>4.15</td>
            <td>2.11.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>16.04</td>
            <td>4.4</td>
            <td>2.11.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
    </tbody>
</table>

## Oracle

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>RHCK</th>
            <th>UEK</th>
            <th>Sensor Version X86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>9.3</td>
            <td>5.14.0-362.13.0.1</td>
            <td>5.15.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>9.2</td>
            <td>5.14.0-284.11.1</td>
            <td>5.15.0</td>
            <td>2.15.0-2.16.0</td>
            <td>2.15.0-2.16.0</td>
        </tr>
        <tr>
            <td>9.1</td>
            <td>5.14.0-162</td>
            <td>5.15.0</td>
            <td>2.14.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>9.0</td>
            <td>5.14.0-162</td>
            <td>5.15.0</td>
            <td>2.14.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.10</td>
            <td>4.18.0</td>
            <td>5.15.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>8.9</td>
            <td>4.18.0-513.5.1</td>
            <td>5.15.0</td>
            <td>2.15.2-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.8</td>
            <td>4.18.0-477.10.1</td>
            <td>5.15.0</td>
            <td>2.15.0-2.16.0</td>
            <td>2.15.0-2.16.0</td>
        </tr>
        <tr>
            <td>8.7</td>
            <td>4.18.0-425.3.1</td>
            <td>5.4.17</td>
            <td>2.14.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.6</td>
            <td>4.18.0-372.9.1</td>
            <td>5.4.17</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.5</td>
            <td>4.18.0-348</td>
            <td>5.4.17</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.4</td>
            <td>4.18.0-305</td>
            <td>5.4.17</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.3</td>
            <td>4.18.0-221</td>
            <td>5.4.17</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.2</td>
            <td>4.18.0-193</td>
            <td>5.4.17</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.1</td>
            <td>4.18.0-147</td>
            <td>N/A</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>8.0</td>
            <td>4.18.0-80</td>
            <td>N/A</td>
            <td>2.10.1-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.9</td>
            <td>3.10.0-1160</td>
            <td>5.4.17</td>
            <td>2.9.1-2.16.0***</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.8</td>
            <td>3.10.0-1127</td>
            <td>4.14.35</td>
            <td>2.8.0-2.16.0**</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.7</td>
            <td>3.10.0-1062</td>
            <td>4.14.35</td>
            <td>2.8.0-2.16.0**</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.6</td>
            <td>3.10.0-957</td>
            <td>4.14.35</td>
            <td>2.8.0-2.16.0**</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.5</td>
            <td>3.10.0-862</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.4</td>
            <td>3.10.0-693</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.3</td>
            <td>3.10.0-514</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.2</td>
            <td>3.10.0-327</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.1</td>
            <td>3.10.0-229</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>7.0</td>
            <td>3.10.0-123</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.16.0</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.10</td>
            <td>2.6.32-754</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.9</td>
            <td>2.6.32-696</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.8</td>
            <td>2.6.32-642</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.7</td>
            <td>2.6.32-573</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
        <tr>
            <td>6.6</td>
            <td>2.6.32-504</td>
            <td class="not-supported">Not Supported</td>
            <td>2.8.0-2.11.3</td>
            <td class="not-supported">Not Supported</td>
        </tr>
    </tbody>
</table>

## Rocky Linux

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>9.3</td>
            <td>5.14.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>9.2</td>
            <td>5.14.0</td>
            <td>2.15.1-2.16.0</td>
            <td>2.15.1-2.16.0</td>
        </tr>
        <tr>
            <td>8.10</td>
            <td>4.18.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>8.9</td>
            <td>4.18.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>8.8</td>
            <td>4.18.0</td>
            <td>2.15.1-2.16.0</td>
            <td>2.15.1-2.16.0</td>
        </tr>
    </tbody>
</table>

## Alma Linux

<table class="sensor-table">
    <thead>
        <tr>
            <th>Distribution</th>
            <th>Kernel Version</th>
            <th>Sensor Version x86_64</th>
            <th>Sensor Version aarch64 (AWS Graviton Processors)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>9.3</td>
            <td>5.14.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>9.2</td>
            <td>5.14.0</td>
            <td>2.15.2-2.16.0</td>
            <td>2.15.2-2.16.0</td>
        </tr>
        <tr>
            <td>8.10</td>
            <td>4.18.0</td>
            <td>2.16.0</td>
            <td>2.16.0</td>
        </tr>
        <tr>
            <td>8.9</td>
            <td>4.18.0</td>
            <td>2.15.2-2.16.0</td>
            <td>2.15.2-2.16.0</td>
        </tr>
        <tr>
            <td>8.8</td>
            <td>4.18.0</td>
            <td>2.15.2-2.16.0</td>
            <td>2.15.2-2.16.0</td>
        </tr>
    </tbody>
</table>
