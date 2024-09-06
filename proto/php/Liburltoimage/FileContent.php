<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: urltoimage/urltoimage.proto

namespace Liburltoimage;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>liburltoimage.FileContent</code>
 */
class FileContent extends \Google\Protobuf\Internal\Message
{
    /**
     *文件名
     *
     * Generated from protobuf field <code>string name = 1;</code>
     */
    protected $name = '';
    /**
     *二进制的文件内容
     *
     * Generated from protobuf field <code>bytes content = 2;</code>
     */
    protected $content = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $name
     *          文件名
     *     @type string $content
     *          二进制的文件内容
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Urltoimage\Urltoimage::initOnce();
        parent::__construct($data);
    }

    /**
     *文件名
     *
     * Generated from protobuf field <code>string name = 1;</code>
     * @return string
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     *文件名
     *
     * Generated from protobuf field <code>string name = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setName($var)
    {
        GPBUtil::checkString($var, True);
        $this->name = $var;

        return $this;
    }

    /**
     *二进制的文件内容
     *
     * Generated from protobuf field <code>bytes content = 2;</code>
     * @return string
     */
    public function getContent()
    {
        return $this->content;
    }

    /**
     *二进制的文件内容
     *
     * Generated from protobuf field <code>bytes content = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setContent($var)
    {
        GPBUtil::checkString($var, False);
        $this->content = $var;

        return $this;
    }

}

